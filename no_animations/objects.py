import pygame as pg
from pygame.locals import *
import constants as cons
import sprites as sp


class Player(pg.sprite.Sprite):
    def __init__(self, position=(0, 0)):
        super().__init__()

        self.image = pg.Surface([cons.player_area[0], cons.player_area[1]])
        self.image.fill(cons.DARK_GREY)
        self.rect = self.image.get_rect(topleft=position)

        self.speed_x = 0
        self.speed_y = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move_right(self):
        self.speed_x = cons.horizontal_speed

    def move_left(self):
        self.speed_x = -1 * cons.horizontal_speed

    def stop(self):
        self.speed_x = 0

    def is_standing(self, floor_group):
        self.rect.y += 1
        collision_list = pg.sprite.spritecollide(self, floor_group, False)
        self.rect.y -= 1

        return len(collision_list) > 0

    def has_hit_ceiling(self, floor_group):
        self.rect.y -= 1
        collision_list = pg.sprite.spritecollide(self, floor_group, False)
        self.rect.y += 1

        return len(collision_list) > 0

    def jump(self, floor_group):
        if self.is_standing(floor_group):
            self.speed_y = cons.jump_speed

    def update_movement(self, floor_group):
        """
        direction é 1 quando o movimento é para a direita e -1 quando é para a esquerda. Desse modo, se a
        tecla apertada for a seta direita, deve-se passar direction = 1. Se for a seta esquerda, deve-se passar
        direction = -1. O default é 1.
        This method will be incremented when collectibles are programmed.
        """

        self.rect.x += self.speed_x
        collision_list = pg.sprite.spritecollide(self, floor_group, False)
        for floor in collision_list:
            if self.speed_x > 0:
                self.rect.right = floor.rect.left
            else:
                self.rect.left = floor.rect.right

        self.rect.y += self.speed_y
        collision_list = pg.sprite.spritecollide(self, floor_group, False)
        for floor in collision_list:
            if self.speed_y < 0:
                self.rect.top = floor.rect.bottom
            else:
                self.rect.bottom = floor.rect.top

        self.calc_gravity(floor_group)

    def update_collecting(self, collectibles_group):
        """collectibles_group will alwats be level.collectibles"""

        collision_list = pg.sprite.spritecollide(self, collectibles_group, True)
        # it is expected that collision_list will always have at most 1
        # item, buit I'll use a for just as a precaution
        if len(collision_list) > 0:
            for item in collision_list:
                # this will romove the sprite from sp.all_sprites
                item.kill()
                item.collected = True

    def update(self, level):
        self.update_movement(level.floors)
        self.update_collecting(level.collectibles)


    def calc_gravity(self, floor_group):
        if not self.is_standing(floor_group):
            if self.has_hit_ceiling(floor_group):
                self.speed_y = 1
            else:
                self.speed_y += cons.gravity
        else:
            self.speed_y = 0


    def teleport_left(self):
        self.rect.x = 0

    def teleport_right(self):
        self.rect.right = cons.width


class Floor(pg.sprite.Sprite):
    def __init__(self, position=(0, 0), area=(50, 50)):
        super().__init__()

        self.image = pg.Surface(area)
        self.image.fill(cons.LIGHT_BLUE)
        self.rect = self.image.get_rect(topleft=position)


class LastingCollectible(pg.sprite.Sprite):
    def __init__(self, center_posit=(18, 18), area=(25, 25)):
        super().__init__()

        self.image = pg.Surface(area)
        self.image.fill(cons.GREEN)
        self.rect = self.image.get_rect(center=center_posit)

        self.collected = False


class TemporaryCollectible(pg.sprite.Sprite):
    def __init__(self, center_posit=(18, 18), area=(15, 15)):
        super().__init__()

        self.image = pg.Surface(area)
        self.image.fill(cons.RED)
        self.rect = self.image.get_rect(center=center_posit)

        self.collected = False


class Level():

    def __init__(self, current_level=1):
        self.current = current_level

        self.floors = sp.all_sprites[current_level]["floors"]
        self.collectibles = sp.all_sprites[current_level]["collectibles"]
        self.npcs = sp.all_sprites[current_level]["npcs"]

    def draw(self, surface):
        self.floors.draw(surface)
        self.collectibles.draw(surface)
        self.npcs.draw(surface)

    def change(self, num):
        self.current += num

        self.floors = pg.sprite.Group(sp.all_sprites[self.current]["floors"])
        self.collectibles = pg.sprite.Group(
            sp.all_sprites[self.current]["collectibles"])
        self.npcs = pg.sprite.Group(sp.all_sprites[self.current]["npcs"])


class Text(pg.font.Font):
    def __init__(self, text, size):
        super().__init__()

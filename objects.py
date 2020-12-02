import sprites as sp
import pygame as pg
import constants as cons
import animations as ani


class AttackSprite(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pg.Surface(cons.attack_area, flags=pg.SRCALPHA)
        self.image.fill(cons.TRANSP_WHITE)
        self.rect = self.image.get_rect(topleft=position)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = ani.char_r
        self.rect = pg.Rect(cons.player_init_posit, cons.player_area)

        self.speed_x = 0
        self.speed_y = 0

        self.walk_count = 0
        self.jumpCount = 0

        self.is_jumping = False
        self.is_double_jumping = False
        self.is_left = False
        self.is_right = True
        self.was_left = False
        self.was_right = False

        self.is_attacking = False
        self.attack_count = 0
        self.attack_wait = -1

        self.HP = 100

    def draw(self, surface):
        if self.walk_count >= 36:
            self.walk_count = 0

        if self.is_jumping and not self.is_left and not self.is_right:
            self.image = ani.jump_s

        elif self.is_jumping and self.is_left:
            self.image = ani.jump_l

        elif self.is_jumping and self.is_right:
            self.image = ani.jump_r

        elif self.is_left and self.speed_x < 0:
            self.image = ani.walkLeft[self.walk_count // 3]
            self.walk_count += 1

        elif self.is_left and self.speed_x == 0:
            self.image = ani.char_l
            self.walk_count = 0

        elif self.is_right and self.speed_x > 0:
            self.image = ani.walkRight[self.walk_count // 3]
            self.walk_count += 1

        elif self.is_right and self.speed_x == 0:
            self.image = ani.char_r
            self.walk_count = 0

        self.image = self.image

        surface.blit(self.image, (self.rect.x-5, self.rect.y-5))
        self.image = ani.char_r

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

        if len(collision_list) > 0:
            self.is_jumping = False
            return True

    def has_hit_ceiling(self, floor_group):
        self.rect.y -= 1
        collision_list = pg.sprite.spritecollide(self, floor_group, False)
        self.rect.y += 1

        return len(collision_list) > 0

    def jump(self):
        self.speed_y = cons.jump1_speed

    def double_jump(self):
        self.speed_y = cons.jump2_speed

    def update_attack(self, enemies_group, attack_box_group):
        attack_box_group.empty()
        # it will take 0.75s for the player to be able to attack
        # again, since the framerate is 60 FPS.
        if 0 <= self.attack_wait <= 44:
            self.attack_wait += 1
        elif self.attack_wait == 45:
            # since self.attack_wait isn't between 0 and 30 when
            # it is equal to -1, the next elif will be able to run
            # and because of that the player will be able to attack
            self.attack_wait = -1

        elif self.is_attacking:
            attack_box = AttackSprite(self.rect.midtop)

            if self.is_right and not self.was_left:
                self.was_right = True
            elif (self.is_left or self.was_left) and not self.was_right:
                attack_box.rect.topright = (
                    attack_box.rect.left+8, attack_box.rect.top)
                self.was_left = True

            attack_box_group.add(attack_box)
            collision_list = pg.sprite.spritecollide(
                attack_box, enemies_group, True)
            for enemy in collision_list:
                enemy.defeated = True
            self.attack_count += 1

            if self.attack_count == 61:
                self.attack_count = 0
                self.is_attacking = False
                self.was_left = False
                self.was_right = False
                self.attack_wait = 0

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

        collision_list = pg.sprite.spritecollide(
            self, collectibles_group, True)
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
        self.update_attack(level.enemies, level.attack_box)

    def update_HP(self, HP_bar, surface):
        # setting how filled the HP bar is at the moment
        if self.HP < 0:
            self.HP = 0
        HP_bar.width = self.HP*(cons.HP_rect[2]/100)

        # drawing the HP bar
        if self.HP >= 1:
            pg.draw.rect(surface, cons.RED, HP_bar, 0, 5)

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

    def teleport_back(self):
        self.rect.topleft = cons.player_init_posit


# The class of platforms. The collision of the player with Floor objects
# is made different from the collision with other types of objects by means
# of the Player.update_movement() method, which only checks for collision
# against Floor objects.
class Floor(pg.sprite.Sprite):
    def __init__(self, position=(0, 0), area=(50, 50)):
        super().__init__()

        self.image = pg.Surface(area)
        self.image.fill(cons.BLUE2)
        self.rect = self.image.get_rect(topleft=position)


class LastingCollectible(pg.sprite.Sprite):
    def __init__(self, center_posit=(18, 18), area=(25, 25)):
        super().__init__()

        self.image = pg.Surface(area)
        self.image.fill(cons.GREEN)
        self.rect = self.image.get_rect(center=center_posit)

        self.collected = False
        self.waiting_for_collection = True


class TemporaryCollectible(pg.sprite.Sprite):
    def __init__(self, center_posit=(18, 18), area=(15, 15)):
        super().__init__()

        self.image = pg.Surface(area)
        self.image.fill(cons.RED)
        self.rect = self.image.get_rect(center=center_posit)

        self.collected = False


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, end, y, vel):
        super().__init__()

        self.walkRight_image = pg.image.load('images/fantasmaR.png')
        self.walkLeft_image = pg.image.load('images/fantasmaL.png')

        self.image = self.walkRight_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.path = (x, end)
        self.vel = vel

        # The time the enemy will take to spawn after its respective level has
        # begun. It is a good thing to somehow associate the instance enemy's
        # drawing, physics and behaviour to self.spawn_time = 0.
        self.spawned = False
        self.defeated = False

    def update(self):
        if self.vel > 0:
            self.image = self.walkRight_image
            if self.rect.x < self.path[1] + self.vel:
                self.rect.x += self.vel
            else:
                self.vel = self.vel * -1
                self.rect.x += self.vel
        else:
            self.image = self.walkLeft_image
            if self.rect.x > self.path[0] - self.vel:
                self.rect.x += self.vel
            else:
                self.vel = self.vel * -1
                self.rect.x += self.vel


class Level():

    def __init__(self, current_level=1):
        self.current = current_level

        self.floors = sp.all_sprites[self.current]["floors"]
        self.collectibles = sp.all_sprites[self.current]["collectibles"]
        self.enemies = sp.all_sprites[self.current]["enemies"]
        self.attack_box = pg.sprite.Group()

    def draw(self, surface):
        self.floors.draw(surface)
        self.collectibles.draw(surface)
        self.enemies.update()
        self.enemies.draw(surface)
        self.attack_box.draw(surface)

    def change(self):
        self.current += 1

        self.floors = sp.all_sprites[self.current]["floors"]
        self.collectibles = sp.all_sprites[self.current]["collectibles"]
        self.enemies = sp.all_sprites[self.current]["enemies"]


base_font = pg.font.Font(None, 30)

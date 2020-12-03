import sprites as sp
import pygame as pg
import constants as cons
import animations as ani
import functions as funcs
import math
import random


class AttackSprite(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.rect = pg.Rect(position, cons.attack_area)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # initial set of the player's texture
        self.image = ani.char_r
        self.rect = pg.Rect(cons.player_init_posit, cons.player_area)

        # control of walking and jumping
        self.speed_x = 0
        self.speed_y = 0
        self.is_jumping = False
        self.is_double_jumping = False

        # control of walking and jumping animation
        self.is_left = False
        self.is_right = True
        self.walk_count = 0
        self.jumpCount = 0
        # control of the direction of the attack
        self.was_left = False
        self.was_right = False

        # control of attacking and taking damage
        self.is_attacking = False
        self.attack_count = 0
        self.attack_wait = -1
        self.damage = 50
        self.has_tk_damage = False
        self.has_tk_damage_count = -1

        # control of shield power up
        self.shield_count = -1

        # collectibles counter
        self.coins_count = 0
        self.hearts_count = 0
        self.shields_count = 0
        self.snowflakes_count = 0

        self.HP = 100

    def draw(self, surface):
        if self.is_attacking and ((self.attack_count == 0 and self.is_left) or self.was_left):
            surface.blit(self.image, (self.rect.x-40, self.rect.y-5))
        else:
            surface.blit(self.image, (self.rect.x-5, self.rect.y-5))
            self.image = ani.char_r

    def set_image(self):
        if not self.is_attacking:

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

        else:
            # see the update_attack() method first
            # in the first frame of the attack, neither self.was_right nor
            # self.was_left are true, so we need to check which texture
            # should be the texture of the player by checking self.is_right
            # and self.is_left
            if not (self.was_right or self.was_left):
                if self.is_right:
                    self.image = ani.punchRight[0]
                else:   # else, self.is_left is true
                    self.image = ani.punchLeft[0]
            else:
                if self.was_right:
                    self.image = ani.punchRight[min(
                        self.attack_count, 11)]
                else:   # else, self.was_left is true
                    self.image = ani.punchLeft[min(self.attack_count, 11)]

        if self.has_tk_damage:
            self.image.set_alpha(
                190 + 30 * math.sin(2 * 3.14 * 0.05 * self.has_tk_damage_count))
        else:
            self.image.set_alpha(255)

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

    def update_attack(self, enemies_group, attack_box_group, collectibles_group):
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

            if self.attack_count <= 61:
                attack_box_group.add(attack_box)
                collision_list = pg.sprite.spritecollide(
                    attack_box, enemies_group, False)
                for enemy in collision_list:
                    enemy.update_dropping(collectibles_group)
                    enemy.kill()
                self.attack_count += 1
            else:
                self.attack_count = 0
                self.is_attacking = False
                self.was_left = False
                self.was_right = False
                self.attack_wait = 0

    def update_tk_damage(self, enemies_group):
        if self.has_tk_damage:
            self.has_tk_damage_count += 1
            if self.has_tk_damage_count == 180:
                self.has_tk_damage_count = -1
                self.has_tk_damage = False

        else:   # else, the player is able to take damage
            self.image.set_alpha(255)
            if len(pg.sprite.spritecollide(self, enemies_group, False)) > 0:
                self.HP -= self.damage
                self.has_tk_damage = True
                self.has_tk_damage_count = 0

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

    def update_collect(self, collectibles_group, enemies_group):
        """collectibles_group will alwats be level.collectibles"""

        collision_list = pg.sprite.spritecollide(
            self, collectibles_group, True)
        # it is expected that collision_list will always have at most 1
        # item, buit I'll use a for just as a precaution
        if len(collision_list) > 0:
            for item in collision_list:
                # this will romove the sprite from sp.all_sprites
                if str(item) == "TemporaryCollectible":
                    item.power_player(self, enemies_group)
                item.kill()
                item.collected = True

    def update_powers(self, surface):
        self.shield_count = funcs.update_count(self.shield_count)

        # updating the shield power
        if self.shield_count != -1:
            player_border_rect = ani.char_r.get_rect()
            player_border_rect.x = self.rect.x - 5
            player_border_rect.y = self.rect.y - 5
            pg.draw.rect(surface, cons.SILVER, player_border_rect, 3)
        else:   # else, shield_count is -1
            self.damage = 50

    def update(self, level, surface):
        self.update_movement(level.floors)
        self.update_collect(level.collectibles, level.enemies)
        self.update_tk_damage(level.enemies)
        self.update_attack(level.enemies, level.attack_box, level.collectibles)
        self.set_image()

    def update_HP(self, HP_bar, surface):
        # setting how filled the HP bar is at the moment
        if self.HP < 0:
            self.HP = 0
        if self.HP > 100:
            self.HP = 100
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
    def __init__(self, image, center_posit=(18, 18)):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(center=center_posit)

        self.collected = False
        self.waiting_for_collection = True

    def __str__(self):
        return "LastingCollectible"


class TemporaryCollectible(pg.sprite.Sprite):
    def __init__(self, item_num, position=(0, 0)):
        super().__init__()

        self.collected = False
        self.num = item_num

        if item_num == 0:
            self.image = ani.coin       # 0 is coin
        elif item_num == 1:
            self.image = ani.heart      # 1 is heart
        elif item_num == 2:
            self.image = ani.snowflake  # 2 is snowflake
        else:
            self.image = ani.shield     # 3 is shield

        self.rect = self.image.get_rect(topleft=position)

    def power_player(self, player, enemies_group):
        if self.num == 0:
            player.coins_count += 1

        if self.num == 1:   # HP pot
            player.HP += 50
            player.hearts_count += 1

        if self.num == 2:   # snowflake
            for enemy in enemies_group:
                enemy.vel = 0
                enemy.freeze_count = 0
            player.snowflakes_count += 1

        elif self.num == 3:  # shield
            player.shield_count = 0
            player.damage = 25
            player.shields_count += 1

    def __str__(self):
        return "TemporaryCollectible"


class Enemy(pg.sprite.Sprite):

    def __init__(self, x, end, y, vel):
        super().__init__()

        self.walkRight_image = ani.ghostR
        self.walkLeft_image = ani.ghostL

        self.image = self.walkRight_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.path = (x, end)
        self.vel = vel
        self.former_vel = vel

        # The time the enemy will take to spawn after its respective level has
        # begun. It is a good thing to somehow associate the instance enemy's
        # drawing, physics and behaviour to self.spawn_time = 0.
        self.defeated = False
        self.done = False

        self.freeze_count = -1

    def drop_item(self, collectibles_group):
        item = TemporaryCollectible(random.randint(0, 3))
        item.rect.center = self.rect.center
        collectibles_group.add(item)

    def update_dropping(self, collectibles_group):
        chance = random.randint(0, 1)
        if chance == 0:
            self.drop_item(collectibles_group)

    def update_movement(self):
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

    def update(self):
        self.update_movement()

        self.freeze_count = funcs.update_count(self.freeze_count)
        if self.freeze_count == 300:
            self.vel = self.former_vel


class Level():

    def __init__(self, current_level=1):
        self.current = current_level

        self.floors = sp.all_sprites[self.current]["floors"]
        self.collectibles = sp.all_sprites[self.current]["collectibles"]
        self.enemies = sp.all_sprites[self.current]["enemies"]
        self.attack_box = pg.sprite.Group()

    def draw(self, surface):
        self.floors.draw(surface)
        self.enemies.update()
        self.enemies.draw(surface)
        self.collectibles.draw(surface)

    def change(self):
        self.current += 1

        self.floors = sp.all_sprites[self.current]["floors"]
        self.collectibles = sp.all_sprites[self.current]["collectibles"]
        self.enemies = sp.all_sprites[self.current]["enemies"]


base_font = pg.font.Font(None, 30)

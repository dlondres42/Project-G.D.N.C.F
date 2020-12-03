import pygame as pg
from pygame.locals import *
import constants as cons
import objects as obj
import animations as ani

player = obj.Player()

# movable platform for creating the platforms of levels
movable_plat = obj.Floor(area=cons.plat14_area)

# HP bar. The first one will be de border, while the second
# will be its filling. The second will be changed throughout
# the game, while the first won't.
HP_bar_border = pg.Rect(cons.HP_rect)
HP_bar = pg.Rect(cons.HP_rect)

# LEVEL 1 SPRITES

# floors
full_ground = obj.Floor(cons.ground_posit, cons.ground_area)
platform1 = obj.Floor(cons.plat1_posit, cons.plat1_area)
platform2 = obj.Floor(cons.plat2_posit, cons.plat2_area)
platform3 = obj.Floor(cons.plat3_posit, cons.plat3_area)
platform4 = obj.Floor(cons.plat4_posit, cons.plat4_area)
platform5 = obj.Floor(cons.plat5_posit, cons.plat5_area)
platform6 = obj.Floor(cons.plat6_posit, cons.plat6_area)
platform7 = obj.Floor(cons.plat7_posit, cons.plat7_area)
platform8 = obj.Floor(cons.plat8_posit, cons.plat8_area)
platform9 = obj.Floor(cons.plat9_posit, cons.plat9_area)

# lasting collectible
attack_col_center = (
    platform5.rect.center[0], platform5.rect.center[0]-80)
attack_col = obj.LastingCollectible(ani.cage1,
                                    center_posit=attack_col_center)


# LEVEL 2 SPRITES

# floors
# full_ground is a floor of level 2
platform10 = obj.Floor(cons.plat10_posit, cons.plat10_area)
platform11 = obj.Floor(cons.plat11_posit, cons.plat11_area)
platform12 = obj.Floor(cons.plat12_posit, cons.plat12_area)
platform13 = obj.Floor(cons.plat13_posit, cons.plat13_area)
platform14 = obj.Floor(cons.plat14_posit, cons.plat14_area)
platform15 = obj.Floor(cons.plat15_posit, cons.plat15_area)
platform16 = obj.Floor(cons.plat16_posit, cons.plat16_area)
platform17 = obj.Floor(cons.plat17_posit, cons.plat17_area)
platform18 = obj.Floor(cons.plat18_posit, cons.plat18_area)
platform19 = obj.Floor(cons.plat19_posit, cons.plat19_area)
platform20 = obj.Floor(cons.plat20_posit, cons.plat20_area)
platform21 = obj.Floor(cons.plat21_posit, cons.plat21_area)
platform22 = obj.Floor(cons.plat22_posit, cons.plat22_area)
platform23 = obj.Floor(cons.plat23_posit, cons.plat23_area)
platform24 = obj.Floor(cons.plat24_posit, cons.plat24_area)
platform25 = obj.Floor(cons.plat25_posit, cons.plat25_area)
platform26 = obj.Floor(cons.plat26_posit, cons.plat26_area)
platform27 = obj.Floor(cons.plat27_posit, cons.plat27_area)
platform28 = obj.Floor(cons.plat28_posit, cons.plat28_area)
platform29 = obj.Floor(cons.plat29_posit, cons.plat29_area)
platform30 = obj.Floor(cons.plat30_posit, cons.plat30_area)
platform31 = obj.Floor(cons.plat31_posit, cons.plat31_area)
platform32 = obj.Floor(cons.plat32_posit, cons.plat32_area)
ceiling = obj.Floor(cons.ceiling_posit, cons.ceiling_area)

# lasting collectible; it will only be added to level.collectibles when all
# enemies of level 2 have been defeated
double_jump_col_center = (
    platform23.rect.center[0], platform23.rect.center[1]+47)
double_jump_col = obj.LastingCollectible(
    ani.cage3, center_posit=double_jump_col_center)

# temporary collectibles
coin1 = obj.TemporaryCollectible(0, cons.coin1)

# enemies
ghost1 = obj.Enemy(cons.ghost1_x, cons.ghost1_end,
                   cons.ghost1_y, cons.ghost1_vel)
ghost2 = obj.Enemy(cons.ghost2_x, cons.ghost2_end,
                   cons.ghost2_y, cons.ghost2_vel)
ghost3 = obj.Enemy(cons.ghost3_x, cons.ghost3_end,
                   cons.ghost3_y, cons.ghost3_vel)
ghost4 = obj.Enemy(cons.ghost4_x, cons.ghost4_end,
                   cons.ghost4_y, cons.ghost4_vel)
ghost5 = obj.Enemy(cons.ghost5_x, cons.ghost5_end,
                   cons.ghost5_y, cons.ghost5_vel)
ghost6 = obj.Enemy(cons.ghost6_x, cons.ghost6_end,
                   cons.ghost6_y, cons.ghost6_vel)
ghost7 = obj.Enemy(cons.ghost7_x, cons.ghost7_end,
                   cons.ghost7_y, cons.ghost7_vel)
ghost8 = obj.Enemy(cons.ghost8_x, cons.ghost8_end,
                   cons.ghost8_y, cons.ghost8_vel)
ghost9 = obj.Enemy(cons.ghost9_x, cons.ghost9_end,
                   cons.ghost9_y, cons.ghost9_vel)
ghost10 = obj.Enemy(cons.ghost10_x, cons.ghost10_end,
                    cons.ghost10_y, cons.ghost10_vel)
ghost11 = obj.Enemy(cons.ghost11_x, cons.ghost11_end,
                    cons.ghost11_y, cons.ghost11_vel)
ghost12 = obj.Enemy(cons.ghost12_x, cons.ghost12_end,
                    cons.ghost12_y, cons.ghost12_vel)
ghost13 = obj.Enemy(cons.ghost13_x, cons.ghost13_end,
                    cons.ghost13_y, cons.ghost13_vel)
ghost14 = obj.Enemy(cons.ghost14_x, cons.ghost14_end,
                    cons.ghost14_y, cons.ghost14_vel)


# LEVEL 3 SPRITES

# floors
half_ground_1 = obj.Floor(cons.half_ground_1_posit, cons.half_ground_1_area)
half_groun_2 = obj.Floor(cons.half_ground_2_posit, cons.half_ground_1_area)
left_wall = obj.Floor(cons.left_wall_posit, cons.left_wall_area)
right_wall = obj.Floor(cons.right_wall_posit, cons.right_wall_area)
upper_platform = obj.Floor(cons.upper_plat_posit, cons.upper_plat_area)
platform33 = obj.Floor(cons.plat33_posit, cons.plat33_area)
platform34 = obj.Floor(cons.plat34_posit, cons.plat34_area)
platform35 = obj.Floor(cons.plat35_posit, cons.plat35_area)
platform36 = obj.Floor(cons.plat36_posit, cons.plat36_area)
platform37 = obj.Floor(cons.plat37_posit, cons.plat37_area)
platform38 = obj.Floor(cons.plat38_posit, cons.plat38_area)
platform39 = obj.Floor(cons.plat39_posit, cons.plat39_area)
platform40 = obj.Floor(cons.plat40_posit, cons.plat40_area)
platform41 = obj.Floor(cons.plat41_posit, cons.plat41_area)
platform42 = obj.Floor(cons.plat42_posit, cons.plat42_area)

# collectible
enhanced_attack_col = obj.LastingCollectible(
    ani.cage6, (upper_platform.rect.centerx, upper_platform.rect.centery-48))

# enemies
ghost15 = obj.Enemy(cons.ghost15_x, cons.ghost15_end,
                    cons.ghost15_y, cons.ghost15_vel)
ghost16 = obj.Enemy(cons.ghost16_x, cons.ghost16_end,
                    cons.ghost16_y, cons.ghost16_vel)
ghost17 = obj.Enemy(cons.ghost17_x, cons.ghost17_end,
                    cons.ghost17_y, cons.ghost17_vel)
ghost18 = obj.Enemy(cons.ghost18_x, cons.ghost18_end,
                    cons.ghost18_y, cons.ghost18_vel)
ghost19 = obj.Enemy(cons.ghost19_x, cons.ghost19_end,
                    cons.ghost19_y, cons.ghost19_vel)
ghost20 = obj.Enemy(cons.ghost20_x, cons.ghost20_end,
                    cons.ghost20_y, cons.ghost20_vel)
ghost21 = obj.Enemy(cons.ghost21_x, cons.ghost21_end,
                    cons.ghost21_y, cons.ghost21_vel)
ghost22 = obj.Enemy(cons.ghost22_x, cons.ghost22_end,
                    cons.ghost22_y, cons.ghost22_vel)

# The following dictionary contains every sprite in the game in the following
# manner: its keys are numbers that relate to each game level. The value of
# each level number is a second dicionary. The velues of that second dicionary
# are the types of sprites that exist in the game, i.e., each second dictionary
# contains the keys "floors", "collectibles" and "enemies", so that, for exemple,
# the value of "floors" are all the floors of the respective level. Thusm for
# exemple, calling all_sprites[1] we access a dictionary of all sprites of
# level 1, so that we can access a tuple with all floors of level 1 with
# all_sprites[1]["floors"]. Similarly, all_sprites[3]["collectibles"] is
# a list of all collectibles of level 3, all_sprites[5]["enemies"] is a tuple
# of all enemies of level 5, and so on. Collectibles are always contained in
# lists so that they can be removed, while floors and enemies are in tuples
# since they may never be removed from all_sprites.

# Another strategy is to make each second depth value to be the Group of
# the sprites the value already contains. This may enhance performance
# but may also require more computer memory.
all_sprites = {
    1: {'floors':       pg.sprite.Group(full_ground, platform1, platform2,
                                        platform3, platform4, platform5,
                                        platform6, platform7, platform8,
                                        platform9),
        'collectibles': pg.sprite.Group(attack_col, coin1),
        'enemies':      pg.sprite.Group()
        },
    2: {'floors':       pg.sprite.Group(full_ground, platform10, platform11,
                                        platform12, platform13, platform14,
                                        platform15, platform16, platform17,
                                        platform18, platform19, platform20,
                                        platform21, platform22, platform23,
                                        platform24, platform25, platform26,
                                        platform27, platform28, platform29,
                                        platform30, platform31, platform32,
                                        ceiling),
        'collectibles': pg.sprite.Group(),
        'enemies':      pg.sprite.Group(ghost1, ghost2, ghost3, ghost4, ghost5,
                                        ghost6, ghost7, ghost8, ghost9,
                                        ghost10, ghost11, ghost12, ghost13,
                                        ghost14)
        },
    3: {'floors':       pg.sprite.Group(movable_plat, half_ground_1, half_groun_2, left_wall,
                                        right_wall, upper_platform, platform33,
                                        platform34, platform35, platform36,
                                        platform37, platform38, platform39,
                                        platform40, platform41, platform42,
                                        ceiling),
        'collectibles': pg.sprite.Group(enhanced_attack_col),
        'enemies':      pg.sprite.Group(ghost15, ghost16, ghost17, ghost18,
                                        ghost19, ghost20, ghost21, ghost22)
        }
}

# The current level variable. At each moment of the game, its attributes
# are pygame Groups containing all the sprites of the level the player is
# currently playing. This level variable is used in main.py to control
# wich sprites must be displayed on the screen wich sprites the player
# must be able to collide with at each moment of the gameplay. "level"'s
# attributes values are changed everytime the player reaches another level.
level = obj.Level()

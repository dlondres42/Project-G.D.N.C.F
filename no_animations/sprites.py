import pygame as pg
from pygame.locals import *
import constants as cons
import objects as obj

pg.init()

player = obj.Player(cons.player_init_posit)

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

# collectible
change_collectible_center = (
    platform5.rect.center[0], platform5.rect.center[0]-70)
change_collectible = obj.LastingCollectible(
    center_posit=change_collectible_center)

# The following dictionary contains every sprite in the game in the following
# manner: its keys are numbers that relate to each game level. The value of
# each level number is a second dicionary. The velues of that second dicionary
# are the types of sprites that exist in the game, i.e., each second dictionary
# contains the keys "floors", "collectibles" and "npcs", so that, for exemple,
# the value of "floors" are all the floors of the respective level. Thusm for
# exemple, calling all_sprites[1] we access a dictionary of all sprites of
# level 1, so that we can access a tuple with all floors of level 1 with
# all_sprites[1]["floors"]. Similarly, all_sprites[3]["collectibles"] is
# a list of all collectibles of level 3, all_sprites[5]["npcs"] is a tuple
# of all npcs of level 5, and so on. Collectibles are always contained in
# lists so that they can be removed, while floors and npcs are in tuples
# since they may never be removed from all_sprites.

# Another strategy is to make each second depth value to be the Group of
# the sprites the value already contains. This may enhance performance
# but may also require more computer memory.
all_sprites = {
    0: {'floors':       pg.sprite.Group(),
        'collectibles': pg.sprite.Group(),
        'npcs':         pg.sprite.Group()
        },
    1: {'floors':       pg.sprite.Group(full_ground, platform1, platform2, platform3,
                                         platform4, platform5, platform6, platform7,
                                         platform8, platform9),
        'collectibles': pg.sprite.Group(change_collectible),
        'npcs':         pg.sprite.Group()
        },
    2: {'floors':       pg.sprite.Group(),
        'collectibles': pg.sprite.Group(),
        'npcs':         pg.sprite.Group()
        },
    3: {'floors':       pg.sprite.Group(),
        'collectibles': pg.sprite.Group(),
        'npcs':         pg.sprite.Group()
        }
}

# The current level variable. At each moment of the game, its attributes
# are pygame Groups containing all the sprites of the level the player is
# currently playing. This level variable is used in main.py to control
# wich sprites must be displayed on the screen wich sprites the player
# must be able to collide with at each moment of the gameplay. "level"'s
# attributes values are changed everytime the player reaches another level.
level = obj.Level()

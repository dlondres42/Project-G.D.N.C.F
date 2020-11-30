# SCREEN
screen = width, height = 1100, 450

# FPS
FPS = 60

# RGB COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
LIGHT_BLUE = (0, 128, 255)
RED = (230, 0, 0)
SILVER = (192, 192, 192)
DARK_GREEN = (0,128,0)
DARK_GREY = (32, 32, 32)
GREEN = (0, 180, 0)

# COORDINATES
# player
player_area = (21, 46)    # witdh and height of player
player_init_posit = (10, height-player_area[1]-45)

# LEVEL 1

# floors
ground_area = (width, height - (player_init_posit[1] + player_area[1]))
ground_posit = (0, height-ground_area[1])
plat1_area = (101, 235)
plat1_posit = (492, 176)
plat2_area = (103, 29)
plat2_posit = (318, 321)
plat3_area = plat2_area
plat3_posit = (172, 236)
plat4_area = plat2_area
plat4_posit = (332, 148)
plat5_area = plat2_area
plat5_posit = (90, 100)
plat6_area = plat2_area
plat6_posit = (920, 327)
plat7_area = plat2_area
plat7_posit = (935, 235)
plat8_area = plat2_area
plat8_posit = (920, 143)
plat9_area = plat2_area
plat9_posit = (935, 52)

# level 1's colelctible is set in the sprites module

# PLAYER MOVEMENT
gravity = 0.4
jump_speed = -8
horizontal_speed = 3

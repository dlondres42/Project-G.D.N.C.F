# SCREEN
screen = width, height = 1100, 450

# FPS
FPS = 60

# RGB COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSP_WHITE = (255, 255, 255, 150)  # RGBA
BLUE = (137, 196, 244)
BLUE2 = (0, 120, 180)     # RGBA
RED = (230, 0, 0)
SILVER = (192, 192, 192)
DARK_GREEN = (0, 128, 0)
DARK_GREY = (32, 32, 32)
GREEN = (0, 180, 0)

# player
player_area = (21, 46)    # witdh and height of player
player_init_posit = (10, height-player_area[1]-45)
attack_area = (55, 46)
HP_rect = (900, 10, 190, 30)

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

# level 1's colelctible is defined in the sprites module

# LEVEL 2

# floors
plat14_posit = (6, 235)
plat14_area = (30, 30)
plat13_posit = (111, 320)
plat13_area = plat14_area

x_dif = plat13_posit[0] - plat14_posit[0]   # 105
y_dif = plat13_posit[1] - plat14_posit[1]   # 85

plat10_posit = (plat13_posit[0] + x_dif, plat13_posit[1] - y_dif)
plat10_area = plat14_area
plat11_posit = (plat10_posit[0] + x_dif, plat10_posit[1] + y_dif)
plat11_area = plat14_area
plat12_posit = (plat11_posit[0] + x_dif, plat11_posit[1] - y_dif)
plat12_area = plat14_area
plat15_posit = (plat12_posit[0] + x_dif, plat12_posit[1] + y_dif)
plat15_area = plat14_area
plat16_posit = (plat15_posit[0] + x_dif, plat15_posit[1] - y_dif)
plat16_area = plat14_area
plat17_posit = (plat16_posit[0] + x_dif, plat16_posit[1] + y_dif)
plat17_area = plat14_area
plat18_posit = (plat17_posit[0] + x_dif, plat17_posit[1] - y_dif)
plat18_area = plat14_area
plat19_posit = (plat18_posit[0] + x_dif, plat18_posit[1] + y_dif)
plat19_area = plat14_area
plat20_posit = (plat19_posit[0] + x_dif, plat19_posit[1] - y_dif)
plat20_area = plat14_area
plat21_posit = (plat13_posit[0], plat13_posit[1] - 2*y_dif)
plat21_area = plat14_area
plat22_posit = (plat11_posit[0], plat11_posit[1] - 2*y_dif)
plat22_area = plat14_area
plat23_posit = (plat15_posit[0], plat15_posit[1] - 2*y_dif)
plat23_area = plat14_area
plat24_posit = (plat17_posit[0], plat17_posit[1] - 2*y_dif)
plat24_area = plat14_area
plat25_posit = (plat19_posit[0], plat19_posit[1] - 2*y_dif)
plat25_area = plat14_area
plat26_posit = (plat14_posit[0], plat14_posit[1] - 2*y_dif)
plat26_area = plat14_area
plat27_posit = (plat10_posit[0], plat10_posit[1] - 2*y_dif)
plat27_area = plat14_area
plat28_posit = (plat12_posit[0], plat12_posit[1] - 2*y_dif)
plat28_area = plat14_area
plat29_posit = (plat14_posit[0], plat14_posit[1] - 2*y_dif)
plat29_area = plat14_area
plat30_posit = (plat16_posit[0], plat16_posit[1] - 2*y_dif)
plat30_area = plat14_area
plat31_posit = (plat18_posit[0], plat18_posit[1] - 2*y_dif)
plat31_area = plat14_area
plat32_posit = (plat20_posit[0], plat20_posit[1] - 2*y_dif)
plat32_area = plat14_area
ceiling_area = (width, 1)
ceiling_posit = (0, -1)

# double jump collectible defined in sprites.py

# enemies
ghost1_x, ghost1_end, ghost1_y, ghost1_vel = (21, 221, 360, 5)
ghost2_x, ghost2_end, ghost2_y, ghost2_vel = (230, 430, 360, 6)
ghost3_x, ghost3_end, ghost3_y, ghost3_vel = (503, 703, 360, 4)
ghost4_x, ghost4_end, ghost4_y, ghost4_vel = (763, 963, 360, 5)


# LEVEL 3

# floors
half_ground_1_posit = (0, height - ground_area[1])   # the same as ground_posit
half_ground_1_area = ((width/2) - 150, ground_area[1])
half_ground_2_posit = ((width/2) + 150, height - ground_area[1])
half_ground_1_area = ((width/2) - 150, ground_area[1])
left_wall_posit = (0, 100)
left_wall_area = (10, height - left_wall_posit[1])
right_wall_area = left_wall_area
right_wall_posit = (width - left_wall_area[0], left_wall_posit[1])
upper_plat_posit = (470, 74)
upper_plat_area = (180, 30)
plat33_posit = (upper_plat_posit[0], upper_plat_posit[1] + upper_plat_area[1] + 50)
plat33_area = upper_plat_area
plat34_posit, plat34_area = (0, 310), (110, 30)
plat35_posit, plat35_area = (290, 230), (30, 30)
plat36_posit, plat36_area = (820, 231), (115, 30)
plat37_posit, plat37_area = (996, 159), (30, 30)
plat38_posit, plat38_area = (0, left_wall_posit[1]), plat34_area
plat39_posit, plat39_area = (290, 72), (30, 30)
plat40_posit, plat40_area = (187, 82), (30, 30)
plat41_posit, plat41_area = (392, 62), (30, 30)
plat42_posit, plat42_area = (630, 371), (30, 30)
# ceiling is a floor of level 3

# level 3's collectible is defined in sprites.py

# PLAYER MOVEMENT
gravity = 0.4
jump1_speed = -8
jump2_speed = -6
horizontal_speed = 3

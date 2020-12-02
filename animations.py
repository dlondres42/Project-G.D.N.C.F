import pygame as pg
from pygame.locals import *

pg.init()

#                IMAGENS DAS ANIMAÇÕES, BACKGROUND E INTRO
###############################################################################
jump_s = pg.image.load('images/standingJUMP.png')
jump_l = pg.image.load('images/LJUMP.png')
jump_r = pg.image.load('images/RJUMP.png')
char_r = pg.image.load('images/standingR.png')
char_l = pg.image.load('images/standingL.png')

walkRight = [pg.image.load('images/R1.png'),  pg.image.load('images/R2.png'),
             pg.image.load('images/R3.png'),  pg.image.load('images/R4.png'),
             pg.image.load('images/R5.png'),  pg.image.load('images/R6.png'),
             pg.image.load('images/R7.png'),  pg.image.load('images/R8.png'),
             pg.image.load('images/R9.png'),  pg.image.load('images/R10.png'),
             pg.image.load('images/R11.png'), pg.image.load('images/R12.png')]

walkLeft = [pg.image.load('images/L1.png'),  pg.image.load('images/L2.png'),
            pg.image.load('images/L3.png'),  pg.image.load('images/L4.png'),
            pg.image.load('images/L5.png'),  pg.image.load('images/L6.png'),
            pg.image.load('images/L7.png'),  pg.image.load('images/L8.png'),
            pg.image.load('images/L9.png'),  pg.image.load('images/L10.png'),
            pg.image.load('images/L11.png'), pg.image.load('images/L12.png')]

background = pg.image.load('images/forest.png')
intro_foto = pg.image.load('images/introfoto.png')

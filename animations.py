import pygame as pg
import functions as funcs
import constants as cons

pg.init()

DISPLAYSURF = pg.display.set_mode(cons.screen)

#                 ANIMAÇÕES DO PLAYER, BACKGROUND E INTRO
###############################################################################
jump_s = pg.image.load('images/standingJUMP.png').convert_alpha()
jump_l = pg.image.load('images/LJUMP.png').convert_alpha()
jump_r = pg.image.load('images/RJUMP.png').convert_alpha()
char_r = pg.image.load('images/standingR.png').convert_alpha()
char_l = pg.image.load('images/standingL.png').convert_alpha()

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

punchRight = [pg.image.load('images/soco1R.png'),
              pg.image.load('images/soco2R.png'),
              pg.image.load('images/soco3R.png'),
              pg.image.load('images/soco4R.png'),
              pg.image.load('images/soco5R.png'),
              pg.image.load('images/soco6R.png'),
              pg.image.load('images/soco7R.png'),
              pg.image.load('images/soco8R.png'),
              pg.image.load('images/soco9R.png'),
              pg.image.load('images/soco10R.png'),
              pg.image.load('images/soco11R.png'),
              pg.image.load('images/soco12R.png')]

punchLeft = [pg.image.load('images/soco1L.png'),
             pg.image.load('images/soco2L.png'),
             pg.image.load('images/soco3L.png'),
             pg.image.load('images/soco4L.png'),
             pg.image.load('images/soco5L.png'),
             pg.image.load('images/soco6L.png'),
             pg.image.load('images/soco7L.png'),
             pg.image.load('images/soco8L.png'),
             pg.image.load('images/soco9L.png'),
             pg.image.load('images/soco10L.png'),
             pg.image.load('images/soco11L.png'),
             pg.image.load('images/soco12L.png')]

background = pg.image.load('images/forest.png')
intro_foto = pg.image.load('images/introfoto.png')

walkRight = funcs.convert_alpha_list(walkRight)
walkLeft = funcs.convert_alpha_list(walkLeft)
punchRight = funcs.convert_alpha_list(punchRight)
punchLeft = funcs.convert_alpha_list(punchLeft)

# COLETÁVEIS

ghostR = pg.image.load('images/fantasmaR.png')
ghostL = pg.image.load('images/fantasmaL.png')
cage1 = pg.image.load('images/Jaula1.png')
cage3 = pg.image.load('images/Jaula3.png')
cage6 = pg.image.load('images/Jaula6.png')

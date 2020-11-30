import sys
import pygame as pg
from pygame.locals import *
import constants as cons
import sprites as sp
import animations as ani
import functions as funcs

# pg.init() is not necessary since the initialization has already been
# done in the animations.py module

# basic configurations
FramesPerSec = pg.time.Clock()

DISPLAYSURF = pg.display.set_mode(cons.screen)
pg.display.set_caption("Project G.D.N.C.F")

pg.event.set_blocked(TEXTINPUT)

# intro musics
pg.mixer.music.load('music/01 -Glorious morning-.mp3')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.5)

# start screen
intro = True
while intro:

    # setting quit option
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        # setting skip of start screen
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pg.mixer.music.stop()
                intro = False

            # setting quit by pressing Esc
            elif event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    DISPLAYSURF.blit(ani.intro_foto, (0, 0))
    FramesPerSec.tick(60)
    pg.display.update()

# gameplay musics
pg.mixer.music.load('music/76677_newgrounds_field_.mp3')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0)    # set to 0.35

# game loop
while True:

    if sp.player.is_standing(sp.level.floors):
        sp.player.is_jumping = False
    else:
        sp.player.is_jumping = True

    # setting quit option
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        # setting player movement control; walk and jump with keyboard arrows
        # or W A S D; it's also possible to jump with SPACE and quit with Esc.
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                sp.player.is_left = True
                sp.player.is_right = False
                sp.player.move_left()

            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                sp.player.is_left = False
                sp.player.is_right = True
                sp.player.move_right()

            elif (event.key == pg.K_UP or event.key == pg.K_w or event.key == pg.K_SPACE) and not sp.player.is_jumping:
                sp.player.jump()

            elif event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

        # setting end of movement when the buttons are unpressed
        elif event.type == pg.KEYUP:
            if (event.key == pg.K_LEFT or event.key == pg.K_a) and sp.player.speed_x < 0:
                sp.player.stop()

            if (event.key == pg.K_RIGHT or event.key == pg.K_d) and sp.player.speed_x > 0:
                sp.player.stop()

    # updating the player's position according to the movement vector
    # generated above
    sp.player.update(sp.level)

    # checking whether the player reached some of the ends of the screen
    # and changing the level if so (provieded he is able to change levels
    # already)
    if sp.player.rect.left < 0:
        sp.player.teleport_right()

    if sp.player.rect.right > cons.width:
        sp.player.teleport_left()

    if sp.attack_col.collected and sp.attack_col.waiting_for_collection:
        sp.level.change()
        sp.player.update(sp.level)
        sp.attack_col.waiting_for_collection = False

    # animating what happened above
    DISPLAYSURF.blit(ani.background, (0, 0))

    if sp.attack_col.collected:
        funcs.draw_text(DISPLAYSURF, (10, 10), "ATTACK ENABLED")

    sp.level.draw(DISPLAYSURF)

    sp.player.draw(DISPLAYSURF)

    pg.display.update()

    # setting the FPS (to 60)
    FramesPerSec.tick(cons.FPS)

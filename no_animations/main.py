import sys
import pygame as pg
from pygame.locals import *
import constants as cons
import sprites as sp

# initiazliation
pg.init()

# basic configurations
FramesPerSec = pg.time.Clock()

DISPLAYSURF = pg.display.set_mode(cons.screen)
pg.display.set_caption("Project G.D.N.C.F")

# pg.event.set_blocked(TEXTINPUT)

# start screen
intro = True
while intro:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                intro = False

    DISPLAYSURF.fill((255, 255, 255))
    pg.display.update()
    FramesPerSec.tick(15)

# game loop
while True:

    # setting quit option
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        # setting player movement control; walk and jump with keyboard arrows or
        # W A S D; you can also quit with Esc.
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                sp.player.move_left()

            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                sp.player.move_right()

            for jump_key in [pg.K_UP, pg.K_w]:
                if event.key == jump_key:
                    sp.player.jump(sp.level.floors)

            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

        # block relating to the collection of the first collectible. when
        # collected, the player becomes able to change levels
            if event.key == pg.K_c and sp.change_collectible.collected:
                cons.level_can_change = not cons.level_can_change

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
    # and changing the level if so
    if sp.player.rect.left < 0:
        sp.player.teleport_right()
        if cons.level_can_change and sp.level.current > min(sp.all_sprites.keys()):
            sp.level.change(-1)
            sp.player.update(sp.level)

    if sp.player.rect.right > cons.width:
        sp.player.teleport_left()
        if cons.level_can_change and sp.level.current < max(sp.all_sprites.keys()):
            sp.level.change(1)
            sp.player.update(sp.level)

    # animating what happened above
    DISPLAYSURF.fill(cons.SILVER)

    sp.player.draw(DISPLAYSURF)

    sp.level.draw(DISPLAYSURF)

    pg.display.update()

    # setting the FPS
    FramesPerSec.tick(cons.FPS)

import sys
import pygame as pg
from pygame.locals import *
import constants as cons
import sprites as sp
import animations as ani
import functions as funcs

# script for creating the platforms of new levels. go to sprites.py and add
# movable_plat to level 3's floors before running this script

# configurações
FramesPerSec = pg.time.Clock()

DISPLAYSURF = pg.display.set_mode(cons.screen)
pg.display.set_caption("Project G.D.N.C.F")

pg.event.set_blocked(TEXTINPUT)

mouse_down = False
move_plat_1 = False
inflat_plat_1 = False

# skipping to level 2
sp.level.change()
sp.level.change()
sp.attack_col.collected = True
sp.double_jump_col.collected = True

# game loop
while True:

    if sp.player.is_standing(sp.level.floors):
        sp.player.is_jumping = False
        sp.player.is_double_jumping = False
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

            elif (event.key == pg.K_UP or event.key == pg.K_w):
                if not sp.player.is_jumping:
                    sp.player.jump()
                elif sp.double_jump_col.collected and not sp.player.is_double_jumping:
                    sp.player.double_jump()
                    sp.player.is_double_jumping = True

            elif event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

            elif sp.attack_col.collected and event.key == pg.K_SPACE:
                sp.player.is_attacking = True

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

    if sp.player.rect.top > cons.height:
        sp.player.teleport_back()
        sp.player.HP -= 50

    if sp.level.current == 1:
        if sp.attack_col.collected:
            sp.level.change()

    if sp.level.current == 2:
        if len(sp.level.enemies) == 0:
            sp.level.collectibles.add(sp.double_jump_col)
        if sp.double_jump_col.collected:
            sp.level.change()

    # animating what happened above
    DISPLAYSURF.blit(ani.background, (0, 0))

    sp.level.draw(DISPLAYSURF)

    # drawing the filling of the HP_bar
    sp.player.update_HP(sp.HP_bar, DISPLAYSURF)

    # drawing the border of the HP bar and the text inside it
    pg.draw.rect(DISPLAYSURF, cons.RED, sp.HP_bar_border, 1, 5)
    funcs.draw_text(
        DISPLAYSURF, f"HP: {sp.player.HP}", ref_rect=sp.HP_bar_border)

    if sp.player.HP == 0:
        game_over = True

    if sp.attack_col.collected:
        funcs.draw_text(DISPLAYSURF, "ATTACK ENABLED", location=(10, 10))
    if sp.double_jump_col.collected:
        funcs.draw_text(DISPLAYSURF, "DOUBLE JUMP ENABLED",
                        location=(10, 40))

    sp.player.draw(DISPLAYSURF)

    pg.display.update()

    # block moving and inflating with mouse

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_e:
            inflat_plat_1 = True

        if event.key == pg.K_m:
            move_plat_1 = True

    elif event.type == pg.KEYUP:
        if event.key == pg.K_e:
            inflat_plat_1 = False

        if event.key == pg.K_m:
            move_plat_1 = False

    if event.type == MOUSEMOTION:
        if move_plat_1:
            sp.movable_plat.rect.center = event.pos

        elif inflat_plat_1:
            x_increase = event.rel[0]
            y_increase = event.rel[1]
            sp.movable_plat.rect.inflate_ip([x_increase, y_increase])
            sp.movable_plat.image = pg.Surface([sp.movable_plat.image.get_width(
            ) + x_increase, sp.movable_plat.image.get_height() + y_increase])
            sp.movable_plat.image.fill(cons.BLUE2)

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_p:
            print(sp.movable_plat.rect)

    # end of block moving and inflating with mouse

    # setting the FPS (to 60)
    FramesPerSec.tick(cons.FPS)

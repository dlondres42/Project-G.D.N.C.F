import pygame as pg
from constants import WHITE


def draw_text(surface, text, color=WHITE, size=30, location=-1, ref_rect=-1):
    text_surface = pg.font.Font(None, size).render(text, True, color)
    if location != -1:
        surface.blit(text_surface, location)
    else:
        text_x_dist = ref_rect.width // 2 - text_surface.get_width() // 2
        text_y_dist = ref_rect.height // 2 - text_surface.get_height() // 2
        surface.blit(text_surface, (ref_rect.x +
                                    text_x_dist, ref_rect.y + text_y_dist))


def convert_alpha_list(lst):
    """ This function makes it possible for all surfaces in lst to be assigned
    an alpha value. It is only used in animations.py """
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i].convert_alpha())

    return new_lst


def update_count(count):
    if count != -1:
        if count == 300:
            count = -1
        else:
            count += 1

    return count

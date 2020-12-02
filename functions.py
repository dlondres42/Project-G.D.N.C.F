from objects import base_font
from constants import WHITE


def draw_text(surface, text, location=-1, ref_rect=-1):
    text_surface = base_font.render(text, True, WHITE)
    if location != -1:
        surface.blit(text_surface, location)
    else:
        text_x_dist = ref_rect.width // 2 - text_surface.get_width() // 2
        text_y_dist = ref_rect.height // 2 - text_surface.get_height() // 2
        surface.blit(text_surface, (ref_rect.x +
                                    text_x_dist, ref_rect.y + text_y_dist))

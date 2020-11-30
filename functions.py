from objects import base_font
from constants import WHITE


def draw_text(surface, location, text):
    text_surface = base_font.render(text, True, WHITE)
    surface.blit(text_surface, location)

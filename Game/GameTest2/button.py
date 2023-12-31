import pygame as pg

class Button:
    def __init__(self, x, y, width, height, color, text, font_size=30):
        self.rect= pg.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pg.font.Font(None, font_size)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

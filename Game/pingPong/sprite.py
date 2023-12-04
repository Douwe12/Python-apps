import pygame as pg

class Sprite(pg.sprite.Sprite):
        def __init__(self, x, y, radius, speed, image_path):
            super().__init__()
            self.x = x
            self.y = y
            self.radius = radius
            self.speed = speed
            self.image = pg.transform.scale(pg.image.load(image_path).convert_alpha(), (radius * 2, radius * 2))
            self.rect = self.image.get_rect()
            self.vector = [-1, 5]

        def move_along_vector(self, multiplier):
            self.x, self.y = self.x + self.vector[0] * multiplier, self.y + self.vector[1] * multiplier
            self.rect.x = self.x
            self.rect.y = self.y
              
              
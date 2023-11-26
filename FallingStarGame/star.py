import pygame as pg

class Star(pg.Rect):
    def __init__(self, x, y, width, height, speed, special):
        super().__init__(x, y, width, height)
        self.speed = speed
        self.special = special
    

    def move_down(self):
        self.y += self.speed
import pygame as pg


class Player(pg.Rect):
    def __init__(self, x, y, size, speed):
        super().__init__(x, y, size, size)
        self.speed = speed

    def move_left(self):
        self.x -= int(self.speed)

    def move_right(self):
        self.x += int(self.speed)
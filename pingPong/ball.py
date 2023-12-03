import pygame as pg

class Ball():
        def __init__(self, x, y, radius, speed):
            self.x = x
            self.y = y
            self.radius = radius
            self.speed = speed

        def move_left(self):
            self.x -= self.speed
        def move_right(self):
             self.x += self.speed
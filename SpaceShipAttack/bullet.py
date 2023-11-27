import pygame as pg
import time
import threading

class Bullet(pg.Rect):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height)
        self.speed = speed
    

    def move_down(self):
        self.y += self.speed

    def move_up(self):
        self.y -= self.speed
    def move_right(self):
        self.x += self.speed
    def move_left(self):
        self.x -= self.speed

    def move_along_vector(self, vector):
        vx, vy = vector

        self.x += (vx * self.speed) 
        self.y += (vy * self.speed)
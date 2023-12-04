import pygame as pg
from vector import Vector
from projectile import Projectile

class Player:
    def __init__(this, x, y, width, height, speed):
        this.x = x
        this.y = y
        this.width = width
        this.height = height
        this.speed = speed

    def shoot_projectile(self):
        start = (self.x, self.y)
        end = (self.x, self.y - 10)
        return (Projectile(self.x, self.y, 40, 40, 0.3), Vector.get_vector(start, end))
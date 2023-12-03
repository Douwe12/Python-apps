import pygame as pg

class Projectile:
    def __init__(this, x, y, width, height, speed):
        this.x = x
        this.y = y
        this.width = width
        this.height = height
        this.speed = speed


    def move_along_vector(self, vector):
        vx, vy = vector

        self.x += (vx * self.speed / 2) 
        self.y += (vy * self.speed / 2)
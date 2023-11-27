import pygame as pg
from bullet import Bullet

class Star(pg.Rect):
    def __init__(self, x, y, width, height, speed, shooting_interval):
        super().__init__(x, y, width, height)
        self.speed = speed
        self.interval = shooting_interval
        self.shoot_timer = 0
    

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

    def shoot_bullet(self, x, y, bullet_width, bullet_height, bullet_speed, bullets):
        if self.shoot_timer > self.interval:
            self.shoot_timer = 0
            bullet = Bullet(x, y, bullet_width, bullet_height, bullet_speed)
            bullets.append((bullet, self))

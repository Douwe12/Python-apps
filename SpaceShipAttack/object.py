import pygame as pg
from bullet import Bullet

class Object(pg.Rect):
    def __init__(self, x, y, width, height, speed, interval):
        super().__init__(x, y, width, height)
        self.speed = speed
        self.interval = interval
        self.shoot_timer = 0

    def shoot_bullet(self, bullet_width, bullet_height, bullet_speed, bullet_interval, bullets):
        if self.shoot_timer > self.interval:
            self.shoot_timer = 0
            bullet = Bullet(self.x, self.y, bullet_width, bullet_height, bullet_speed, bullet_interval)
            bullets.append(bullet)
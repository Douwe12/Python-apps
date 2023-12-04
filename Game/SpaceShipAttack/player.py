import pygame as pg
from object import Object


class Player(Object):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height)
        self.speed = speed
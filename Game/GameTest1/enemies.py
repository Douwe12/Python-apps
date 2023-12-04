import pygame as pg
import sys
from entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, size, speed):
        super().__init__(x, y, size, speed)

    def target_entity(self, target):
        pass


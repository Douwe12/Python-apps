import pygame as pg
import sys
from entity import Entity


class Player(Entity):
    def __init__(self, x, y, size, speed):
        super().__init__(x, y, size, speed)
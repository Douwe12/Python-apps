import math
import sys
import pygame as pg

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def get_vector(cls, start, target):
        x1, y1 = start
        x2, y2 = target

        return cls(x2 - x1, y2 - y1).normalize()

    def normalize(self):
        x, y = self.x, self.y
        lenght = math.sqrt(x**2 + y**2)

        if lenght == 0:
            return (0, 0)
        else:
            return (x / lenght, y / lenght)
        
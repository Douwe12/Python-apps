import pygame as pg
import sys
import math

class Entity:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def get_location(self):
        return (self.x, self.y)
    
    def set_location(self, x, y):
        self.x = x
        self.y = y

    def move_along_vector(self, vector):
        vx, vy = vector

        self.x += (vx * self.speed) 
        self.y += (vy * self.speed)

    def check_collide(self, object):
        closest_x = max(object.x - object.size / 2, min(self.x, object.x + object.size / 2))
        closest_y = max(object.y - object.size / 2, min(self.y, object.y + object.size / 2))

        # Calculate the distance between the center of the self and the closest point on the object
        distance_x = self.x - closest_x
        distance_y = self.y - closest_y
        distance_squared = distance_x**2 + distance_y**2

        # Check if the distance is less than the radius of the self
        return distance_squared <= (self.size**2)



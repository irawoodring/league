import csv
import math
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

sys.path.append('../')
import league


class SideScrollCamera:

    def __init__(self, width, height, center_on, drawables, world_size):
        self.width = width
        self.height = height
        self.center_on = center_on
        self.drawables = drawables
        self.x = self.center_on.x
        self.y = self.center_on.y
        self.world_size = world_size

    def update(self, time):
        print('x:', self.x)
        print('player x: ',self.center_on.x)
        print('adj pos:', (self.x + (self.width * .75)))
        print('adj minus pos:', (self.x - (self.width * .9)))
        if self.center_on.x > (self.x + (self.width * .75)) or self.center_on.x < (self.x - (self.width * .9)) :
            if self.x < self.center_on.x:
                self.x += (self.width * .02)
            else:
                self.x -= (self.width * .02)
            offset_x = - self.x + (self.width * .01)

            for d in self.drawables:
                d.rect.x = d.x + offset_x

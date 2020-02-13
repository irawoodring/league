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
        print('x:', round(self.x))
        print('player x: ',round(self.center_on.x))
        print('adj pos:', round(self.x + (self.width)))
        print('adj minus pos:', round(self.x - self.width))
        print('velocity:    ', round(self.center_on.velocity[0]))
        if self.center_on.x > (self.x + (self.width)) or self.center_on.x < (self.x - (self.width)):
            # if self.center_on.x > self.x:
            self.x += round(self.center_on.velocity[0] * (self.width * .02))
            # else:
            #     self.x += round(self.center_on.velocity[0] * (self.width * .02))
            offset_x = - (self.x - (self.width // 2))

            for d in self.drawables:
                d.rect.x = d.x + offset_x

import csv
import math
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

sys.path.append('../')
import league


class SideScrollCamera(league.UGameObject):

    def __init__(self, width, height, center_on, drawables, world_size):
        self.width = width
        self.height = height
        self.center_on = center_on
        self.drawables = drawables
        self.x = self.center_on.x
        self.y = self.center_on.y
        self.world_size = world_size

        # draw a window around the center to determine when to move the camera
        self.window_left = self.center_on.x - (self.width * .15)
        self.window_right = self.center_on.x + (self.width * .15)

    def update(self, time):

        if self.center_on.x - self.width // 2 > 0 and self.center_on.x + self.width // 2 < self.world_size[0] - 16 and \
            self.center_on.x < self.window_left or \
            self.center_on.x > self.window_right:
            # self.x = self.center_on.x
            # self.y = self.center_on.y
            self.x += self.center_on.velocity[0] * (self.width * .05)

            ## reset our movement "buffer"
            self.window_left = self.center_on.x - (self.width * .15)
            self.window_right = self.center_on.x + (self.width * .15)
        offset_x = - (self.x - (self.width // 2))
        
        for d in self.drawables:
            if hasattr(d, 'static'):
                continue
            d.rect.x = d.x + offset_x

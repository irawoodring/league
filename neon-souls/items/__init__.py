"""A Generic Item"""
import os
import sys
import pygame

sys.path.append('..')
from league import DUGameObject

class Item(DUGameObject):
    def __init__(self, image_path, x, y, layer=3):
        super().__init__(self)
        self._layer = layer
        self.width = 20
        self.height = 25
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.top = self.y - 3
        self.animating_up = False

    def grab(self, player):
        pass

    def update(self, delta_time):
        if not self.alive():
            self.rect = pygame.Rect(0, 0, 0, 0)
            return
        if self.y <= self.top:
            self.animating_up = False
        if self.y >= self.top + 6:
            self.animating_up = True

        if self.animating_up:
            self.y -= (6 * delta_time)
        else:
            self.y += (6 * delta_time)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


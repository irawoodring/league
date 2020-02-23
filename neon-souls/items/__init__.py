"""A Generic Item"""
import os
import sys
import pygame

sys.path.append('..')
from league import DUGameObject

class Item(DUGameObject):
    """Contains generic properties for an animated game item"""
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
        """To be overridden to create affect in-game

        Args:
            player (actors.Player): player instance to apply effects to
        """
        pass

    def update(self, delta_time):
        """Create bouncing animation and correctly set rect for collision
        
        Args:
            delta_time (float): time to adjust for when calculating frames/movement
        """
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


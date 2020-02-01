import pygame
import league

class Projectile(league.Character):
    def __init__(self,x,y,image):
        super().__init__()
        self._layer = 50
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, time):
        self.rect.x = self.rect.x + 1

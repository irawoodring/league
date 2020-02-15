import sys
sys.path.append('../../')
import pygame
from league import Character

class Projectile(Character):
    def __init__(self,x,y):
        super().__init__()
        self._layer = 50
        self.image = pygame.image.load('./assets/shot-2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, time):
        self.rect.x = self.rect.x + 1

    
    
    

import sys
sys.path.append('../../')
import pygame
import neon_engine
from league import Character
from league import GameObject

class Projectile(Character):
    def __init__(self,x,y):
        super().__init__()
        self._layer = 50
        self.image = pygame.image.load('./assets/shot-2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, time):
        self.rect.x = self.rect.x + 5

    
class Weapon(GameObject):
    def __init__(self, character, engine):
        super().__init__()
        self.character = character
        self.x = character.x
        self.y = character.y
        self.projectiles = []
        self.engine = engine
    
    def fire(self, inputs):
        if inputs['SPACE'] is True:
            p = Projectile(self.x, self.y)
            self.engine.objects.append(p)
            self.engine.drawables.add(p)
        
    

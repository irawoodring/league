import sys
sys.path.append('../../')
import pygame
import neon_engine
from actors import ActorBase
from league import GameObject

class Projectile(ActorBase):
    def __init__(self, image_path, image_size, x, y, z):
        super().__init__(self, image_path, image_size, z=z, x=x, y=y)
        self._layer = 50
        
    def update(self, time):
        #Use velocity
        self.rect.x = self.rect.x + 5

    
class Weapon(GameObject):
    def __init__(self, character):
        super().__init__()
        self.character = character
        self.x = character.x
        self.y = character.y
        self.projectiles = []
        
    
    #def fire(self, inputs):
        #if inputs['SPACE'] is True:
            #p = Projectile(self.x, self.y)
            #self.engine.objects.append(p)
            #self.engine.drawables.add(p)
        
    

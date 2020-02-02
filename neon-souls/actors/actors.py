import sys
sys.path.append('../../')

from abc import ABC
import pygame

from league import Character
from league import Drawable

class ActorBase(ABC, Character):
    def __init__(self, image_path, image_size, z=0, x=0, y=0):
        super().__init__(z=z, x=x, y=y)

        self.delta = 512 # What is this value doing?

        self.x = x
        self.y = y

        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, image_size)
        except FileNotFoundError as file_error:
            raise FileNotFoundError('{} was not found'.format(image_path))

        self.rect = self.image.get_rect()
        
        self.blocks = pygame.sprite.Group()

        self.collide_function = pygame.sprite.collide_rect()
        self.collisions = []

        self.collider = Drawable()
        self.collider.image = pygame.Surface([Settings.tile_size, Setting.tile_size])
        self.collider.rect = self.collider.image.get_rect()

class Player(ActorBase):
    def __init__(self, image_path, image_size, z=0, x=0, y=0):
        super().__init__(image_path, image_size, z=z, x=x, y=y)
        self.velocity = ()
    



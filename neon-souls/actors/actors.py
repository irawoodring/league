import sys
sys.path.append('../../')

from abc import ABC
import pygame

from league import Character
from league import OffScreenException
from league import Drawable
from league import Settings
from physics import GravityBound, GravityManager

import logging

logger = logging.getLogger('Player')

class ActorBase(Character):
    def __init__(self, image_path, image_size, z=0, x=0, y=0):
        super().__init__(z=z, x=x, y=y)

        #self.delta = 512 # What is this value doing?

        self.x = x
        self.y = y

        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, image_size)
        except FileNotFoundError as file_error:
            raise FileNotFoundError('{} was not found'.format(image_path))

        self.rect = self.image.get_rect()
        
        self.blocks = pygame.sprite.Group()

        self.collide_function = pygame.sprite.collide_circle
        self.collisions = []

        self.collider = Drawable()
        self.collider.image = pygame.Surface([Settings.tile_size, Settings.tile_size])
        self.collider.rect = self.collider.image.get_rect()

class Player(ActorBase, GravityBound):
    def __init__(self, image_path, image_size, gravity_region, z=0, x=0, y=0):
        super().__init__(image_path, image_size, z=z, x=x, y=y)
        self.velocity = [0,0]
        self.speed = 100
        self.gravity_region = gravity_region

    def move_player(self, time, inputs):
        amount = self.speed * time
        if inputs['W'] is True:
            self.velocity[1] = -amount
        else: 
            self.velocity[1] = 0

        # XOR Statement
        # https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html
        # If either key is pressed BUT not both @ the same time.
        if inputs['D'] ^ inputs['A']:
            if inputs['D'] is True:
                self.velocity[0] = amount
            elif inputs['A'] is True:
                self.velocity[0] = -amount
        else:
            self.velocity[0] = 0

        try:
            if not self.in_world():
                raise OffScreenException
            else:
                self.x = self.x + self.velocity[0]
                self.y = self.y + self.velocity[1]
                self.update(0)
                # TODO: manage collisions
        except:
            pass

        self.velocity = [0,0]

    def in_world(self):
        """
        Todo Check that we are still in the world
        """
        return True

    def update(self, time):
        self.rect.x = self.x
        self.rect.y = self.y
        self.collisions = []
        for sprite in self.blocks:
            self.collider.rect.x = sprite.x
            self.collider.rect.y = sprite.y
            if pygame.sprite.collide_rect(self, self.collider):
                self.collisions.append(sprite)
    
    def process_gravity(self, time):
        gravity_manager = GravityManager.get_instance()
        gravity = gravity_manager.get_gravity(self.gravity_region)
        grav_amount = (gravity[0] * time, gravity[1] * time)
        self.velocity[0] = self.velocity[0] + grav_amount[0]
        self.velocity[1] = self.velocity[1] + grav_amount[1]
        
        # logger.debug('velocity: {}'.format(self.velocity))
        try:
            if not self.in_world():
                raise OffScreenException
            else:
                self.x = self.x + self.velocity[0]
                self.y = self.y + self.velocity[1]
                self.update(0)
                # TODO: manage collisions
        except:
            pass

        self.velocity = [0,0]


    


    



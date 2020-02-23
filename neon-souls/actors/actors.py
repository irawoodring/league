import sys
sys.path.append('../../')

from abc import ABC
import pygame
import math

from league import Character
from league import OffScreenException
from league import Drawable
from league import Settings
from physics import GravityBound, GravityManager
from .animation import WalkingAnimatedSprite, ConstantAnimatedSprite
from mechanics import Health

import logging

logger = logging.getLogger('actor')

class ActorBase(Character):
    def __init__(self, image_path, image_size, z=0, x=0, y=0):
        super().__init__(z=z, x=x, y=y)

        self.x = x
        self.y = y
        self.image_size = image_size

        if image_path is None:
            self.image = None
        else:
            try:
                self.image = pygame.image.load(image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, image_size)
            except FileNotFoundError as file_error:
                raise FileNotFoundError('{} was not found'.format(image_path))

            self.rect = self.image.get_rect()
            
            self.blocks = pygame.sprite.Group()

        self.collide_function = pygame.sprite.collide_rect
        self.collisions = []

        self.collider = Drawable()
        self.collider.image = pygame.Surface([Settings.tile_size, Settings.tile_size])
        self.collider.rect = self.collider.image.get_rect()
    
    def handle_map_collisions(self):
        for collision in self.collisions:
            bot = bool(collision.rect.collidepoint(self.rect.midbottom))
            top = bool(collision.rect.collidepoint(self.rect.midtop))
            right = bool(collision.rect.collidepoint(self.rect.midright))
            left = bool(collision.rect.collidepoint(self.rect.midleft))

            # # stop on bot or top
            self.velocity[1] = 0 if bot and self.velocity[1] > 0 else self.velocity[1]
            self.velocity[1] = 0 if top and self.velocity[1] < 0 else self.velocity[1]
            

            self.velocity[0] = 0 if right and self.velocity[0] > 0 else self.velocity[0]
            self.velocity[0] = 0 if left and self.velocity[0] < 0 else self.velocity[0]

class Player(ActorBase, GravityBound):
    MAX_JUMP_VELOCITY = -10
    MAX_FALL_VELOCITY = 20
    def __init__(self, static_image_path, walking_sprite_path, image_size, gravity_region, z=0, x=0, y=0, layer=5):
        super().__init__(None, image_size, z=z, x=x, y=y)
        self._layer = layer
        self.velocity = [0,0]
        self.speed = 200
        self.gravity_region = gravity_region
        self.facing_left = False

        self.sprite_manager = WalkingAnimatedSprite(static_image_path, walking_sprite_path)
        self.get_image([0,0])
        self.blocks = pygame.sprite.Group()

        self.heath = Health(3, 1)

    def move_player(self, time, inputs):
        amount = self.speed * time
        if inputs['W'] is True:
            jump_velocity = self.velocity[1] - amount
            self.velocity[1] = jump_velocity \
                if jump_velocity >= self.MAX_JUMP_VELOCITY else self.MAX_JUMP_VELOCITY

        if self.velocity[1] > self.MAX_FALL_VELOCITY:
            self.velocity[1] = self.MAX_FALL_VELOCITY        

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

        ## PUT THIS AFTER ALL the calculations
        if True in inputs.values():
            self.facing_left = self.velocity[0] < 0

        self.get_image(self.velocity)

    def in_world(self):
        """
        Todo Check that we are still in the world
        """
        return True

    def update(self, time):
        # For some reason the rect object is position at 0,0 at the start of every update function.
        self.rect.x = self.x
        self.rect.y = self.y
        self.handle_map_collisions()
        
        self.x = self.x + self.velocity[0]
        self.y = self.y + self.velocity[1]
        self.rect.x = self.x
        self.rect.y = self.y

        # self.collisions = []
        for sprite in self.blocks:
            self.collider.rect.x = sprite.x
            self.collider.rect.y = sprite.y
            if pygame.sprite.collide_rect(self, self.collider):
                self.collisions.append(sprite)

        if self.heath.at_zero():
            pass # We'll do something later when we have finished. other sections 
    
    def process_gravity(self, time, gravity_vector):
        gravity_vector = (gravity_vector[0] * time, gravity_vector[1] * time)

        # Right now we ignore a horizontal gravity cause we can't handle
        # it right now
        # self.velocity[0] = self.velocity[0] + gravity_vector[0]
        self.velocity[1] = self.velocity[1] + gravity_vector[1]

    def get_gravity_name(self):
        return self.gravity_region

    def get_image(self, vector):
        if vector[0] == 0:
            self.image = self.sprite_manager.get_static_image(self.facing_left).convert_alpha()
        else:
            self.image = self.sprite_manager.get_walking_image(self.facing_left)

        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()
    

class SentinalEnemy(ActorBase):
    def __init__(self, sprite_loader_path, player_instance, image_size, patrol_list, z=0, x=0, y=0, speed=100, layer=5):
        super().__init__(None, image_size, z=z, x=x, y=y)
        self._layer = layer
        self.velocity = [0,0]
        self.speed = speed
        self.facing_left = False

        self.patrol_list = patrol_list
        self.current_patrol_point = patrol_list[0]
        self.patrol_index = 0
        self.player = player_instance
        
        self.sprite_manager = ConstantAnimatedSprite(sprite_loader_path)
        self.image = self.sprite_manager.get_sprite(self.facing_left)
        self.blocks = pygame.sprite.Group()

    def update(self, deta_game_time):
        # For some reason the rect object is position at 0,0 at the start of every update function.
        self.rect.x = self.x
        self.rect.y = self.y
        self.determine_move(deta_game_time)
        self.get_image(self.velocity)

        self.x = self.x + self.velocity[0]
        self.y = self.y + self.velocity[1]
        self.rect.x = self.x
        self.rect.y = self.y

        # self.collisions = []
        # for sprite in self.blocks:
        #     self.collider.rect.x = sprite.x
        #     self.collider.rect.y = sprite.y
        #     if pygame.sprite.collide_rect(self, self.collider):
        #         self.collisions.append(sprite)

    def determine_move(self, delta_game_time):
        # player_distance = SentinalEnemy.get_distance(self.x, self.player.x, self.y, self.player.y)
        self.update_patrol_point()
        dist_from_x = self.current_patrol_point[0] - self.x
        if dist_from_x < 0:
            amount = -self.speed * delta_game_time
            self.velocity = [amount, 0]
        else:
            amount = self.speed * delta_game_time
            self.velocity = [amount, 0]

    def get_distance(x1, x2, y1, y2):
        return math.sqrt(((x2-x1)**2) + ((y2 - y1)**2))
    
    def update_patrol_point(self):
        dist_from_x = self.current_patrol_point[0] - self.x
        if abs(dist_from_x) < 25:
            self.patrol_index = (self.patrol_index + 1) % len(self.patrol_list)
            self.current_patrol_point = self.patrol_list[self.patrol_index]

    def get_image(self, vector):
        self.facing_left = True if self.velocity[0] < 0 else False
        self.image = self.sprite_manager.get_sprite(self.facing_left)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()

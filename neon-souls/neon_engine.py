import sys
sys.path.append('../')

from league import Engine
import pygame
import logging
from copy import deepcopy
logger = logging.getLogger('NeonEngine')

class NeonEngine(Engine):
    MOVE_KEYS = (pygame.K_w, pygame.K_a, pygame.K_d)
    BASE_MOVE_STATE = {'W': False, 'A': False, 'D': False, 'W_new': False }
    def __init__(self, title):
        super().__init__(title)

        self.movement_inputs = deepcopy(self.BASE_MOVE_STATE)
        self.movement_function = None
        #self.checked_movement_inputs = False

    # def _handle_inputs(self):
    #     super().handle_inputs()
    #     self.movement_inputs = deepcopy(self.BASE_MOVE_STATE)
    #     for event in pygame.event.get():
    #         logger.debug(event)
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_w:
    #                 self.movement_inputs['W'] = True
    #             elif event.key == pygame.K_d:
    #                 self.movement_inputs['D'] = True
    #             elif event.key == pygame.K_a:
    #                 self.movement_inputs['A'] = True
    #             else:
    #                 logger.debug(event)
            
    #     #Call the movement function
    #     self.movement_function(self.game_delta_time, self.movement_inputs)

# Multi key press info came from https://stackoverflow.com/questions/37121511/can-i-press-two-keys-simultaneously-for-a-single-event-using-pygame
    def handle_inputs(self):
        self.movement_inputs = deepcopy(self.BASE_MOVE_STATE)

        keys_pressed = pygame.key.get_pressed()
        self.movement_inputs['W'] = bool(keys_pressed[pygame.K_w])
        self.movement_inputs['D'] = bool(keys_pressed[pygame.K_d])
        self.movement_inputs['A'] = bool(keys_pressed[pygame.K_a])

        for event in pygame.event.get():
            # logger.debug(event)
            # Check "normal" events
            if event.type in self.events.keys():
                self.events[event.type](self.game_delta_time)
            # Check if these key_event keys were pressed
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_events.keys():
                    self.key_events[event.key](self.game_delta_time)


        if True in self.movement_inputs.values():
            logger.debug('Move called')
            self.movement_function(self.game_delta_time, self.movement_inputs)


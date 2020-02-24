import sys
sys.path.append('../')

from league import Engine, Settings
import pygame
import logging
from copy import deepcopy
logger = logging.getLogger('NeonEngine')

class NeonEngine(Engine):
    """
    The base engine wasn't designed for a side scroller. Side scrollers need
    more refined input controls. With that in mind we implemented a new engine 
    that inherited the old one and made tweeks to allow for better movement 
    control
    """
    MOVE_KEYS = (pygame.K_w, pygame.K_a, pygame.K_d)
    ACTION_KEYS = (pygame.K_SPACE)

    BASE_MOVE_STATE = {'W': False, 'A': False, 'D': False, 'W_new': False }
    BASE_ACTION_STATE = {'SPACE': False}

    def __init__(self, title):
        """
        Inits the neon engine. Does all the same stuff as old engine. In addition
        added new members to better handle movement. includeing a dedicated
        function reference to whatever the players function is for handling 
        input

        param - title: The title of the game 
        <sarcasm> I wonder what we're calling this game </sarcasm>
        """
        super().__init__(title)

        self.movement_inputs = deepcopy(self.BASE_MOVE_STATE)
        self.movement_function = None

        self.action_inputs = deepcopy(self.BASE_ACTION_STATE)
        self.action_function = None

        self.physics_functions = []

    # Multi key press info came from https://stackoverflow.com/questions/37121511/can-i-press-two-keys-simultaneously-for-a-single-event-using-pygame
    def handle_inputs(self):
        """
        Overrides old input handling. Non movement key presses are handled
        just like before. Additionally Movement inputs 
        are handled per movement key. 

        The whole keypress arry is checked and each corresponding movement key 
        updates a boolean flag in a dict that represents what keys are pressed 
        at any given time.
        """
        self.movement_inputs = deepcopy(self.BASE_MOVE_STATE)
        self.action_functions = deepcopy(self.BASE_ACTION_STATE)

        keys_pressed = pygame.key.get_pressed()
        self.movement_inputs['W'] = bool(keys_pressed[pygame.K_w])
        self.movement_inputs['D'] = bool(keys_pressed[pygame.K_d])
        self.movement_inputs['A'] = bool(keys_pressed[pygame.K_a])

        self.action_inputs['SPACE'] = bool(keys_pressed[pygame.K_SPACE])

        for event in pygame.event.get():
            # logger.debug(event)
            # Check "normal" events
            if event.type in self.events.keys():
                self.events[event.type](self.game_delta_time)
            # Check if these key_event keys were pressed
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_events.keys():
                    self.key_events[event.key](self.game_delta_time)

        self.movement_function(self.game_delta_time, self.movement_inputs)
        self.action_function(self, self.action_inputs)



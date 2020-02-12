import sys
sys.path.append('../')

from league import Engine, Settings
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
        self.physics_functions = []

    def run(self):
        """
        The main game loop. This game loop overrides the original game loop to 
        track physics state on objects during each iteration. 
        """
        self.running = True
        while self.running:
        # The time since the last check
            now = pygame.time.get_ticks()
            self.real_delta_time = now - self.last_checked_time
            self.last_checked_time = now
            self.game_delta_time = self.real_delta_time * (0.001 * Settings.gameTimeFactor)

            # Wipe screen
            self.screen.fill(Settings.fill_color)

            self.handle_physics()

            # Process inputs
            self.handle_inputs()

            # Update game world
            # Each object must have an update(time) method
            self.check_collisions()
            for o in self.objects:
                o.update(self.game_delta_time)

            # Generate outputs
            #d.update()
            self.drawables.draw(self.screen)

            # Show statistics?
            if self.visible_statistics:
                self.show_statistics()

            # Could keep track of rectangles and update here, but eh.
            pygame.display.flip()

            # Frame limiting code
            self.clock.tick(Settings.fps)

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
            self.movement_function(self.game_delta_time, self.movement_inputs)

    def handle_physics(self):
        for function in self.physics_functions:
            function(self.game_delta_time)


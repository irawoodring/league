import sys
sys.path.append('../')

from league import Engine
import pygame

class NeonEngine(Engine):
    MOVE_KEYS = (pygame.K_w, pygame.K_a, pygame.K_d)
    def __init__(self, title):
        super().__init__(title)

        self.movement_inputs = {'W': False, 'A': False, 'D': False, 'W_new': False }
        self.movement_function = None
        #self.checked_movement_inputs = False

    def handle_inputs(self):
        return super().handle_inputs()
        movement_events = [event for event in pygame.events.get() 
        if event.key in self.MOVE_KEYS and event.type == pygame.KEYDOWN]
        for move in movement_events:
            if move.key == pygame.K_w:
                self.movement_inputs['W'] = True
            elif move.key == pygame.K_d:
                self.movement_inputs['D'] = True
            else:
                self.movement_inputs['A'] = True

        #Call the movement function
        self.movement_function(self.game_delta_time, self.movement_inputs)

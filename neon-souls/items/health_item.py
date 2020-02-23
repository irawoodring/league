"""A Generic Item to add to player health"""
import pygame
from . import Item

class HealthItem(Item):
    def __init__(self, image_path, x, y, layer=3):
        super(HealthItem, self).__init__(image_path, x, y)
        self.heal_amount = 10

    def grab(self, player):
        player.health.gain_health(self.heal_amount)
        effect = pygame.mixer.Sound('./assets/health-sound.wav')
        effect.play()
        self.kill()

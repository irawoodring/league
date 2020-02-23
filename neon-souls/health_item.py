import league
import pygame
from mechanics.health import Health

class HealthItem(league.DUGameObject):
    def __init__(self, image_path, x, y, player, layer=3):
        super().__init__(self)
        self._layer = layer
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (league.Settings.width, league.Settings.height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.heal_amount = 10

    def heal(self):
        player.health.gain_health(self.heal_amount)

    def update(self, deltaTime):
        if self.rect.colliderect(player.rect):
            self.heal()


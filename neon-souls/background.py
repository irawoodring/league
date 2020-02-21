import league
import pygame

class Background(league.DGameObject):
    def __init__(self, image_path, layer=0):
        super().__init__(self)
        self._layer = layer
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (league.Settings.width, league.Settings.height))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.rect.x = 000
        self.rect.y = 0
        self.static = True

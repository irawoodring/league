import pygame


class AnimatedSpriteBase:
    def __init__(self, static_image_path):
        self.static_image = pygame.image.load(static_image_path)

    def get_static_image(self, reversed=False):
        if reversed:
            return pygame.transform.flip(self.static_image, True, False)
        return self.static_image

class WalkingAnimatedSprite(AnimatedSpriteBase):
    def __init__(self, static_image_path, walking_sprite_list):
        super().__init__(static_image_path)

        self.index = 0
        self.walking_images = tuple([pygame.image.load(walking_sprite) for walking_sprite in walking_sprite_list])

    def get_walking_image(self, reversed=False):
        walking_image = self.walking_images[self.index]
        self.index = (self.index + 1) % len(self.walking_images)

        if reversed: 
            return pygame.transform.flip(walking_image, True, False)
        
        return walking_image
import pygame

"""
Holds a collection of sprite managing classes that allow for 
an actor to have dynamic sprites based on thier situation

Author: David Baas
Date: 2/22/2020
"""

class AnimatedSpriteBase:
    """
    Base class of all animated sprites. Holds a single sprite for a static actor
    """

    def __init__(self, static_image_path):
        """
        Initializes base class. If specified finds a static image sprite. 
        Useful for standing still.

        param - static_image_path: The path to the single sprite.
        """

        if static_image_path is not None:
            self.static_image = pygame.image.load(static_image_path)

    def get_static_image(self, reversed=False):
        """
        Returns the static image. 

        There is no error checking if the static image is none. If called when
        static image is none. The programmer is in for a fun time.

        param - reversed: Flips the sprites around to have it face left
        return: self.static_image
        """
        if reversed:
            return pygame.transform.flip(self.static_image, True, False)
        return self.static_image


class ConstantAnimatedSprite(AnimatedSpriteBase):
    """
    Some actors have a constant sprite loop. This class allows for a single 
    list of sprite paths that can be updated at the will of the game engine
    """
    def __init__(self, sprite_loader_path):
        """
        Inits the class. Will send None for the static image since the class is
        for constantly animated actors. 

        param - sprite_loader_path a list of sprites in the constant animation loop 
        """
        super().__init__(None)
        
        self.index = 0
        self.image_rotation = tuple([pygame.image.load(sprite) for sprite in sprite_loader_path])

    def get_sprite(self, reversed = False):
        """
        Gets the next sprite in the animation loop. 

        param - reversed: returns the sprite flipped if set to true
        return: the next sprite in the animation loop. 
        """
        image = self.image_rotation[self.index]
        self.index = (self.index + 1) % len(self.image_rotation)

        if reversed: 
            return pygame.transform.flip(image, True, False)
        
        return image
        

class WalkingAnimatedSprite(AnimatedSpriteBase):
    """
    Walking animated sprites. Used by the player. Allows for a standing still 
    static sprite and a walking animation loop. 
    """

    def __init__(self, static_image_path, walking_sprite_list):
        """
        Inits the WalkingAnimatedSprite Adds a second list of sprites 
        for the walking componenet.

        param - static_image_path: Path to sprite for when actor is standing still
        param - walking_sprite_list: List of paths for actors movement loop.
        """
        super().__init__(static_image_path)

        self.index = 0
        self.walking_images = tuple([pygame.image.load(walking_sprite) for walking_sprite in walking_sprite_list])

    def get_walking_image(self, reversed=False):
        """
        Get the next image in the movement loop

        param - reversed: returns the sprite flipped if set to true
        return: the next sprite in the animation loop. 
        """
        walking_image = self.walking_images[self.index]
        self.index = (self.index + 1) % len(self.walking_images)

        if reversed: 
            return pygame.transform.flip(walking_image, True, False)
        
        return walking_image
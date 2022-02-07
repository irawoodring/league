# Multiple inheritance constructor call issue fixed, thanks to:
# https://stackoverflow.com/questions/26927571/multiple-inheritance-in-python3-with-different-signatures
#
import pygame
import abc

class GameObject():
    """Any object that makes up our game world."""
    def __init__(self):
        self.tags = []
        self.name = None
        self.x = 0.0
        self.y = 0.0

class UGameObject(GameObject):
    """A game object that is updateable but not drawn."""
    def __init__(self):
        super().__init__()

    def update():
        pass

class Drawable(GameObject, pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.DirtySprite.__init__(self)

class DGameObject(Drawable):
    """A game object that is drawable, but not updateable.  A static object."""
    def __init__(self):
        super().__init__()


class DUGameObject(UGameObject, Drawable):
    """A game object that is updateable and drawable."""
    def __init__(self):
        super().__init__()
        pygame.sprite.DirtySprite.__init__(self)

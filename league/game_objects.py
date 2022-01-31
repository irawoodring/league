# abstract base classes
import abc
import pygame

class GameObject(abc.ABC):
    """Any object that makes up our game world."""
    pass

class Drawable(pygame.sprite.Sprite):
    """Creates a drawable.  For us, a drawable is a pygame Sprite object."""
    def __init__(self, x=0, y=0, layer=0):
        super().__init__()
        self.image = None
        self.rect = None
        self.x = x
        self.y = y
        self._layer = layer

class Updateable(abc.ABC):
    """An interface that ensures an object has an update(gameDeltaTime) method."""
    @abc.abstractmethod
    def update(gameDeltaTime):
        pass

class UGameObject(GameObject, Updateable):
    """A game object that is updateable but not drawn."""
    pass

class DGameObject(GameObject, Drawable):
    """A game object that is drawable, but not updateable.  A static object."""
    pass

class DUGameObject(UGameObject, Drawable):
    """A game object that is updateable and drawable."""
    pass

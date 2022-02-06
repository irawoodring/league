import pygame as pg

class Scene:
    def __init__(self, name):
        self.name = name
        self.updateables = []
        self.drawables = pg.sprite.LayeredDirty()
        self.fps = 30
        self.music = None

    def set_fps(fps):
        self.fps = fps

#!/usr/bin/env python3

import sys

sys.path.append("../league")

from engine import *
from scene import *
import pygame as pg

engine = Engine("Simple Zombie Scene")
scene = Scene("Scene One")
scene.fps = 60
zombie = pg.sprite.DirtySprite()
zombie.image = pygame.image.load("../assets/zombie/female/Attack (1).png")
zombie.rect = zombie.image.get_rect()
zombie.dirty = 2
scene.drawables.add(zombie)
scene.fill_color = (0, 65, 101)
engine.scene = scene
engine.toggle_statistics()
engine.run()
pg.quit()

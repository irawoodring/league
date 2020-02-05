#!/usr/bin/env python3

import pygame
import sys
sys.path.append('..')
import league
from background import Background

"""
Copied and modified from example.
"""
def init_map(engine):
    """Create map and background"""
    league.Settings.tile_size = 16
    league.Settings.fill_color = (31, 38, 84)
    sprites = league.Spritesheet('./assets/tileset-collapsed.png', league.Settings.tile_size, 14)
    level1 = league.Tilemap('./assets/level1.lvl', sprites, layer = 2)
    engine.drawables.add(level1.passable.sprites()) 
    full_background = Background('./assets/skyline-a.png', 0)
    background = Background('./assets/buildings-bg.png', 1)
    engine.drawables.add(full_background)
    engine.drawables.add(background)
    # world_size = (level1.wide*league.Settings.tile_size, level1.high*league.Settings.tile_size)
    # cam = league.LessDumbCamera(800, 600, player, engine.drawables, world_size)
    # engine.objects.append(cam)



def main():
    e = league.Engine("Neon Souls")
    e.init_pygame()

    # create background and level
    init_map(e)

    
    e.events[pygame.QUIT] = e.stop
    e.run()

if __name__=='__main__':
    main()

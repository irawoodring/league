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
    level1 = league.Tilemap('./assets/level1.lvl', sprites, layer = 1)
    world_size = (level1.wide*league.Settings.tile_size, level1.high*league.Settings.tile_size)
    engine.drawables.add(level1.passable.sprites()) 
    background = Background('./assets/near-buildings-bg.png')
    engine.drawables.add(background)

def main():
    e = league.Engine("Neon Souls")
    e.init_pygame()

    # create background and level
    init_map(e)

    
    e.events[pygame.QUIT] = e.stop
    e.run()

if __name__=='__main__':
    main()

#!/usr/bin/env python3

import pygame
import sys
sys.path.append('../')
import league
from background import Background
from actors import Player
from physics import GravityManager
import neon_engine


"""
Copied and modified from example.
"""
def init_map(engine, player):
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
    world_size = (level1.wide*league.Settings.tile_size, level1.high*league.Settings.tile_size)
    # cam = league.LessDumbCamera(400, 200, player, engine.drawables, world_size)
    # engine.objects.append(cam)
    player.world_size = world_size
    player.rect = player.image.get_rect()
    player.blocks.add(level1.impassable)
    engine.objects.append(player)
    engine.drawables.add(player)

def main():
    engine = neon_engine.NeonEngine('Neon Souls')
    
    engine.init_pygame()

    player = Player('./assets/idle-1.png',(128, 128), 'default', 2, 300, 450)

    gravity_manager = GravityManager.get_instance()
    print(gravity_manager)

    gravity_manager.add_gravity('default', (0, 50))
    
    # create background and level
    init_map(engine, player)

    pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // league.Settings.gameTimeFactor)
    # e.key_events[pygame.K_a] = p.move_left
    # e.key_events[pygame.K_d] = p.move_right
    # e.key_events[pygame.K_w] = p.move_up
    # e.key_events[pygame.K_s] = p.move_down
    engine.movement_function = player.move_player
    engine.physics_functions.append(player.process_gravity)

    engine.events[pygame.QUIT] = engine.stop
    engine.run()

if __name__=='__main__':
    league.logger_init()
    main()

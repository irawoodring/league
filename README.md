# L.E.A.G.U.E.

Laker Educationally Accessible Game Understanding Engine is an engine built on top of PyGame to teach basic game development aspects.

Code for this engine is written to mirror pseudocode in *Game Programming Algorithms and Techniques* by Madhav.

Note that this was designed with education in mind.  Therefore optimization is not of the essence.  We will not (for instance) use concepts like DirtySprites or updating only parts of the screen, relying instead upon a more traditional (easier to understand albeit less optimal) approach.  This may mean renaming certain pygame concepts to keep closer to the textbook code.

**Be sure you are using Python 3.**

# Classes

**Engine** - the core game engine.  No game logic should go here, merely the game loop.

The engine handles events, calls update(deltaTime) on all updateable objects (held in self.objects) and draws all objects in self.drawables.

**Graphics** - a utility class for graphics functions.  Includes tilemaps, spritesheets, and cameras.

**Settings** - a static class used to hold default values needed by the Engine class.  Be sure to set values to your game's values before starting the engine.


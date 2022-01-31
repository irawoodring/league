import abc
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Engine:
    """Engine is the definition of our game engine.  We want it to
    be as game agnostic as possible, and will try to emulate code
    from the book as much as possible.  If there are deviations they
    will be noted here.

    Fields:
    title - The name of the game.
    running - Whether or not the engine is currently in the main game loop.
    clock - The real world clock for elapsed time.
    events - A dictionary of events and handling functions.
    key_events - A dictionary of events and handling functions for KEYDOWN events.
                 Please note that the backtick (`) key is default.
    objects - A list of updateable game objects.
    drawables - A list of drawable game objects.
    screen - The window we are drawing upon.
    real_delta_time - How much clock time has passed since our last check.
    game_delta_time - How much game time has passed since our last check.
    visible_statistics - Whether to show engine statistics statistics.
    statistics_font - Which font to use for engine stats
    collisions = A dictionary of objects that can collide, and the function to call when they do. 
    """
    
    delta_time = 0

    def __init__(self, title, width=1024, height=768):
        self.title = title
        self.running = False
        self.visible_statistics = False
        self.width = width
        self.height = height
        self.init_pygame()

    def init_pygame(self):
        """This function sets up the state of the pygame system,
        including passing any specific settings to it."""
        # Startup the pygame system
        pygame.init()
        # Create our window
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Set the title that will display at the top of the window.
        pygame.display.set_caption(self.title)
        # Create the clock
        self.clock = pygame.time.Clock()
        self.last_checked_time = pygame.time.get_ticks()
        # Startup the joystick system
        pygame.joystick.init()
        # For each joystick we find, initialize the stick
        for i in range(pygame.joystick.get_count()):
            pygame.joystick.Joystick(i).init()
        # Set the repeat delay for key presses
        pygame.key.set_repeat(500)
        # Create statistics font
        self.statistics_font = pygame.font.Font(None,30)

    def run(self):
        """The main game loop.  As close to our book code as possible."""
        self.running = True
        while self.running:
            # The time since the last check
            now = pygame.time.get_ticks()
            delta_time = now - self.last_checked_time
            self.last_checked_time = now

            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Wipe screen
            self.screen.fill(self.scene.fill_color)
            
            # Generate outputs
            self.scene.drawables.draw(self.screen)

            # Show statistics?
            if self.visible_statistics:
                self.show_statistics()
            
            # Could keep track of rectangles and update here, but eh.
            pygame.display.flip()

            # Frame limiting code
            self.clock.tick(self.scene.fps)

    # Show/Hide the engine statistics
    def toggle_statistics(self):
        self.visible_statistics = not self.visible_statistics

    # If we are to show that statistics, draw them with this function
    def show_statistics(self):
        statistics_string = "Version: " + str("1.0.0")
        statistics_string = statistics_string +  " FPS: " + str(int(self.clock.get_fps()))
        fps = self.statistics_font.render(statistics_string, True, (255, 255, 255))
        self.screen.blit(fps, (10, 10))
    
    # Toggle the engine to stop
    def stop(self, time):
        self.running = False

    # Shutdown pygame
    def end(self, time):
        pygame.quit()

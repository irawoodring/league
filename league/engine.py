import abc
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Engine:
    """Engine is the definition of our game engine.  We want it to
    be as game agnostic as possible, and will try to emulate code
    from the book as much as possible.  If there are deviations they
    will be noted here.
    """
    
    """delta_time is the elapsed time since the last frame in ms"""
    delta_time = 0
    """events is the current set of events for this frame.  Allows GameObjects to check events themselves."""
    events = None
    """current_scene is the scene we are currently running"""
    current_scene = None

    """We must provide a title for the window, and can optionally
    provide a width and/or height."""
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
        # Allow pausing
        self.paused = False

    def run(self):
        """The main game loop.  As close to our book code as possible."""
        self.running = True
        if Engine.current_scene.music:
            pygame.mixer.music.load(Engine.current_scene.music)
            pygame.mixer.music.play(-1)
        while self.running:
            # The time since the last check
            #now = pygame.time.get_ticks()
            #delta_time = now - self.last_checked_time
            #self.last_checked_time = now

            # Check events
            Engine.events = pygame.event.get()
            #if len(Engine.events) > 0:
            #    print(Engine.events)
            for event in Engine.events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                        pygame.mixer.music.unpause()

            if self.paused:
                pygame.mixer.music.pause()
                Engine.delta_time = self.clock.tick(Engine.current_scene.fps) / 1000.0 # percentage of a second
                continue

            # Update updateables
            for o in Engine.current_scene.updateables:
                o.update()

            # Wipe screen
            self.screen.fill(Engine.current_scene.fill_color)
            
            # Generate outputs
            Engine.current_scene.drawables.draw(self.screen)

            # Show statistics?
            if self.visible_statistics:
                self.show_statistics()
            
            # Could keep track of rectangles and update here, but eh.
            pygame.display.flip()

            # Frame limiting code
            Engine.delta_time = self.clock.tick(Engine.current_scene.fps) / 1000.0 # percentage of a second

    # Show/Hide the engine statistics
    def toggle_statistics(self):
        self.visible_statistics = not self.visible_statistics

    # If we are to show that statistics, draw them with this function
    def show_statistics(self):
        statistics_string = "Version: " + str("1.0.0")
        statistics_string = statistics_string +  " FPS: " + str(int(self.clock.get_fps()))
        fps = self.statistics_font.render(statistics_string, True, (255, 255, 255))
        self.screen.blit(fps, (10, 10))
    
    # Shutdown pygame
    def end(self):
        pygame.mixer.music.stop()
        pygame.quit()

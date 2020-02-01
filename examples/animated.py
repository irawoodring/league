class Player(Drawable):
    def __init__(self, x, y):
        super().__init__(None, 100, x, y)
        self.step_count = 0
        self.images = {}
        self.direction = Direction.RIGHT    
        self.state = State.IDLE
        self.state_time = pygame.time.get_ticks()
        self.images[State.IDLE] = self.load_images("./assets/ninja/IDLE__00") 
        self.images[State.ATTACK] = self.load_images("./assets/ninja/ATTACK__00")
        self.images[State.THROW] = self.load_images("./assets/ninja/THROW__00")
        self.images[State.RUN] = self.load_images("./assets/ninja/RUN__00")
        self.image = self.images[State.IDLE][Direction.RIGHT][0]
        self.frame = 0

    def update_image(self):
        if self.state != State.RUN:
            self.image = self.images[self.state][self.direction][self.frame % 10]
        else:
            self.image = self.images[self.state][self.direction][self.step_count]
        #print("Image #" + str(self.frame % 10))
        #print(str(self.state) + " facing " + str(self.direction) + " #" + str(self.step_count))

    def move_up(self):
        self.switch_state(State.RUN)
        self.y = self.y - Settings.tile_size // 2

    def move_down(self):
        self.switch_state(State.RUN)
        self.y = self.y + Settings.tile_size // 2

    def move_left(self):
        self.switch_state(State.RUN)
        if self.direction == Direction.RIGHT:
            self.switch_dir(Direction.LEFT)
        else:
            self.step_count = (self.step_count + 1) % 10
        self.x = self.x - Settings.tile_size // 2
        self.update_image()

    def move_right(self):
        self.switch_state(State.RUN)
        if self.direction == Direction.LEFT:
            self.switch_dir(Direction.RIGHT)
        else:
            self.step_count = (self.step_count + 1) % 10
        self.x = self.x + Settings.tile_size // 2
        self.update_image()

    def reset_idle(self):
        time = pygame.time.get_ticks()
        elapsed = time - self.state_time
        if elapsed > 100 and self.state == State.RUN:
            self.switch_state(State.IDLE)

    def switch_state(self, state):
        time = pygame.time.get_ticks()
        if self.state != state:
            self.state = state
            self.state_time = time

    def switch_dir(self, direction):
        self.direction = direction
        self.step_count = 0
        
    def load_images(self, path):
        images = {}
        right = {}
        left = {}
        for i in range(0, 10):
            p = path + str(i) + ".png"
            #print("Loading " + p)
            temp = pygame.image.load(p).convert_alpha()
            #temp = pygame.transform.scale(temp, (Settings.tile_size, Settings.tile_size))
            temp = pygame.transform.scale(temp, (Settings.tile_size * 2, Settings.tile_size * 2))
            right[i] = temp 
            left[i] = pygame.transform.flip(temp, True, False)
        images[Direction.RIGHT] = right
        images[Direction.LEFT] = left
        return images

    def update(self):
        self.frame = (self.frame + 1) % Settings.fps
        self.image = self.images[self.state][self.direction][self.frame % 10]


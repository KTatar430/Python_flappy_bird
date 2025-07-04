import pygame

class Pipe:
    def __init__(self, x, height):
        self.x = x  # Position of the pipe on the x-axis
        self.height = height  
        self.width = 52
        self.gap = 100
        self.passed = False  # Flag to check if the pipe has been passed by the bird

        self.pipe_image = pygame.image.load('src/assets/pipe.png').convert_alpha()
        self.pipe_image = pygame.transform.scale(self.pipe_image, (self.width, 320))  # scale if needed
        self.pipe_top = pygame.transform.flip(self.pipe_image, False, True)

    def move(self, speed):
        self.x -= speed  # Move pipe to left by "speed" pixels

        self.pipe_top = pygame.transform.flip(self.pipe_image, False, True)

    def draw(self, surface):
        # Draw top pipe (flipped)
        top_y = self.height - self.pipe_top.get_height()
        surface.blit(self.pipe_top, (self.x, top_y))

        # Draw bottom pipe (normal)
        bottom_y = self.height + self.gap
        surface.blit(self.pipe_image, (self.x, bottom_y))
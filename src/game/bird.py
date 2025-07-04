import pygame  

class Bird:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  
        self.radius = 15  # Bird hitbox as a circle
        self.velocity = 0  # Vertical speed of the bird
        self.gravity = 0.5  # Gravitational acceleration
        self.jump_strength = -8  # Jump strength
        
        self.image = pygame.image.load('src/assets/bird.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (self.radius * 3, self.radius * 3)) # Scaling the bird image to fit the hitbox
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def flap(self):
        self.velocity = self.jump_strength 

    def update(self):
        self.velocity += self.gravity  
        self.y += self.velocity  
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, screen):
        # Draw the bird on the screen
        screen.blit(self.image, self.rect)

        bird_rect = pygame.Rect(self.x - self.radius/2, self.y - self.radius/2, self.radius , self.radius)
        #pygame.draw.rect(screen, (255, 0, 0), bird_rect, 2)

    def collides_with(self, pipe):
        # Rectangle hitbox for the bird
        bird_rect = pygame.Rect(self.x - self.radius/2, self.y - self.radius/2, self.radius, self.radius)
        

        top_pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.height)
        bottom_pipe_rect = pygame.Rect(pipe.x, pipe.height + pipe.gap, pipe.width, 480 - (pipe.height + pipe.gap))
        
        # Check for collision with pipes
        return bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect)
import pygame

class Base:
    def __init__(self, y_position):
        self.y_position = y_position  
        self.height = 80  

    def draw(self, surface):
    
        pygame.draw.rect(surface, (222, 184, 135), (0, self.y_position, 320, self.height))

    def update(self):
        pass  # Can add base movement logic
import pygame  
from game.game_loop import start_game_loop  

def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 480))
    pygame.display.set_caption("Flappy Bird Clone")

    start_game_loop(screen)  

if __name__ == "__main__":
    main()
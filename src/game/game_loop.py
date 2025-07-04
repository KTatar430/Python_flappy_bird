import pygame  
import random  
import torch

from game.bird import Bird  
from game.pipe import Pipe  
from game.base import Base  
from game.FlappyBird_MLP import FlappyBird_MLP

PLAYER_MODE = True

# Use GPU if possible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the model once
mlp_model = FlappyBird_MLP(device).to(device)
mlp_model.eval()

class DummySound:
    def play(self): pass
    def set_volume(self, volume): pass

def start_game_loop(screen):
    clock = pygame.time.Clock()
    font1 = pygame.font.SysFont(None, 48)  
    font2 = pygame.font.SysFont(None, 32)

    try:
        flap_sound = pygame.mixer.Sound('src/assets/flap.wav')
    except FileNotFoundError:
        flap_sound = DummySound()
    flap_sound.set_volume(0.15)

    try:
        death_sound = pygame.mixer.Sound('src/assets/death.wav')
    except FileNotFoundError:
        death_sound = DummySound()
    death_sound.set_volume(0.3)

    background = pygame.image.load('src/assets/background.png').convert()
    bg_width = background.get_width()

    while True:
        bird = Bird(60, 240)  
        pipes = [Pipe(320, random.randint(100, 300))]  
        base = Base(400)  
        speed = 3   
        running = True
        score = 0
        bg_x = 0

        while running:
            if PLAYER_MODE:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            bird.flap()
                            flap_sound.play()
            else:
                # AI mode: prepare input tensor for the model
                data = torch.tensor([
                    bird.x, bird.y, bird.velocity, pipes[0].x, pipes[0].height
                ], dtype=torch.float32).to(device)
                with torch.no_grad():
                    output = mlp_model(data)
                    action = int(output.item() > 0.5)  # 1 if output > 0.5 else 0
                if action == 1:
                    bird.flap()
                    flap_sound.play()
                # Still allow quitting in AI mode
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

            bird.update()

            for pipe in pipes:
                pipe.move(speed)
                if not pipe.passed and pipe.x + pipe.width < bird.x:
                    pipe.passed = True
                    score += 1

            if pipes[-1].x < 150:
                pipes.append(Pipe(320, random.randint(100, 300)))
            if pipes[0].x + pipes[0].width < 0:
                pipes.pop(0)

            for pipe in pipes:
                if bird.collides_with(pipe):
                    death_sound.play()
                    running = False

            if bird.y - bird.radius < 0 or bird.y + bird.radius > base.y_position:
                death_sound.play()
                running = False

            # Move and draw background
            bg_x -= speed / 3
            if bg_x <= -bg_width:
                bg_x += bg_width
            screen.blit(background, (int(bg_x), 0))
            screen.blit(background, (int(bg_x) + bg_width, 0))

            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)
            base.draw(screen)

            score_text = font2.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)

        # --- Game Over Screen ---
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_over = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

            # Transparent overlay for game over
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            text1 = font1.render("Game Over!", True, (255, 0, 0))
            text2 = font1.render("SPACE - Retry", True, (255, 255, 255))
            text3 = font1.render("ESC - Quit", True, (255, 255, 255))
            text4 = font1.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(text1, (60, 140))
            screen.blit(text2, (40, 240))
            screen.blit(text3, (65, 290))
            screen.blit(text4, (90, 190))
            pygame.display.flip()
            clock.tick(30)
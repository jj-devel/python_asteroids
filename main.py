import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = 60
    while True:
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((00, 00, 00))
        pygame.display.flip()
        clock.tick(FPS)
        dt = clock.get_time() / 1000 
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import *

def main():
    pygame.init()

    # main() function calls
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = 60
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2),)

    # Game loop
    while True:
        # Call for game loop exit protocol
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((00, 00, 00))

        # Main section of game loop
        player.draw(screen)

        # End section of game loop
        pygame.display.flip()
        clock.tick(FPS)
        dt = clock.get_time() / 1000 
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()

    # Groups: 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # main() function calls
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = 60
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2),)
    asteroid_field = AsteroidField()


    # Game loop
    while True:
        # Call for game loop exit protocol
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((00, 00, 00))

        # Main section of game loop
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
            # Collision between player and asteroids
        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                print("Game over!")
                sys.exit()
            # Collision between shot and asteroid
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        # End section of game loop
        pygame.display.flip()
        clock.tick(FPS)
        dt = clock.get_time() / 1000 
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

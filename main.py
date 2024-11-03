# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# get our constants
# module import could be listing or wildcard
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    # groups to hold game entities in
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # define groups for game entitites
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    # used variables and game entities
    dt = 0.0 # delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # input updates
        for entity in updateable:
            entity.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid): # ship hitting asteroid
                print("Game Over!")
                exit()
                
            for shot in shots:
                if shot.is_colliding(asteroid): # bullet hitting asteroid
                    shot.kill()
                    asteroid.split()
                
        # additional events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # on quit event
                return

        # draw frame
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        
         # expose frame, then pause to update at 60 FPS
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
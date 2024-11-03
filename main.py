# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player

# get our constants
# module import could be listing or wildcard
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 # delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_char = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updateable = pygame.sprite.Group(player_char)
    drawable = pygame.sprite.Group(player_char)

    while True:
        # input updates
        for entity in updateable:
            entity.update(dt)

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
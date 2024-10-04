# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    game_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for obj_updatable in updatable:
            obj_updatable.update(dt)
            for obj_asteroid in asteroids:
                if obj_asteroid.checkcollision(game_player):
                    print("Game over!")
                    sys.exit()
                for obj_shot in shots:
                    if obj_asteroid.checkcollision(obj_shot):
                        obj_shot.kill()
                        obj_asteroid.split()
        for obj_drawable in drawable:
            obj_drawable.draw(screen)
        # game_player.update(dt)        
        # game_player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    return

if __name__ == "__main__":
    main()
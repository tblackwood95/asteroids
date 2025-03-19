import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroid_field = AsteroidField()

    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill((0, 0, 0))   
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
        for entity in drawable:
            entity.draw(screen)
        for shot in shots:
            shot.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
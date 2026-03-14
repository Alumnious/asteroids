import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    #game settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #game clock
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable,drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable)

    #AsteroidField
    AF = AsteroidField()
    #Player
    my_player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT /2)
    #game loop
    game_on = True
    while game_on == True:

        #ability to close out of game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #log tracking
        log_state()
        #render settings
        screen.fill("black")
        #draw needs to be between fill and flip
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(my_player) == True:
                log_event("player_hit")
                print ("Game over!")
                return sys.exit()
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()

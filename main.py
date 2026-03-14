import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
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
        my_player.update(dt)
        my_player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()

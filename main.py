import pygame
from scripts.configs import WINDOW_NAME, SCREEN_WIDTH, SCREEN_HEIGHT, FPS


pygame.init()

def main():
    pygame.display.set_caption(WINDOW_NAME)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True


    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.flip()
    

    pygame.quit()

if __name__ == '__main__':
    main()
import pygame
import settings

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    
    pygame.display.flip()
    clock.tick(settings.FPS)


pygame.quit()
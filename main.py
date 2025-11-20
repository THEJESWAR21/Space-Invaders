import pygame
import settings
import scripts.player as player

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.WINDOW_NAME)
clock = pygame.time.Clock()
running = True


while running:

    # Draw the Player into the Screen
    player.draw_player(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() # Draw the frame and display it
    dt = clock.tick(settings.FPS) / 1000 # Framerate


pygame.quit()


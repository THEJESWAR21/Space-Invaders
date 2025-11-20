import pygame
import settings
import scripts.player as player

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.WINDOW_NAME)
clock = pygame.time.Clock()

player.player_load()

running = True


while running:
    dt = clock.tick(settings.FPS) / 1000 # Framerate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    player.player_control(dt)
    player.draw_player(screen)

    pygame.display.flip() # Draw the frame and display it


pygame.quit()


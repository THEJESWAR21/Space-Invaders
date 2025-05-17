import pygame
from pygame.locals import *
import os

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
framerate = 60

player = pygame.image.load(os.path.join('assets', 'Player.png'))

player_width = player.get_width()
player_height = player.get_height()

player = pygame.transform.scale(player, (player_width * 0.4, player_height * 0.4))



x_pos = 700
y_pos = 600

running = True
while running:

    screen.fill(0)
    screen.blit(player, (x_pos,y_pos))


    # EXIT Functionality
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed_is = pygame.key.get_pressed()

    if key_pressed_is[K_LEFT] or key_pressed_is[K_a]:
        x_pos -= 5
    if key_pressed_is[K_RIGHT] or key_pressed_is[K_d]:
        x_pos += 5


    clock.tick(framerate) # FrameRate
    pygame.display.flip()

pygame.quit()

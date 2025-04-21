import pygame
import os


# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = pygame.image.load('./assets/Player.png')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    

pygame.display.flip()

clock.tick(60) # Framerate
pygame.quit()
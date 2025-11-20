import pygame
import os
import settings

PLAYER_IMG_PATH = os.path.join("assets","Player.png") 

def player_load():
    global player, player_rect
    player = pygame.image.load(PLAYER_IMG_PATH).convert_alpha() # Load Player Image
    player_rect = player.get_rect() # Gets the Image Rect Position
    player_rect.center = (settings.PLAYER_X, settings.PLAYER_Y)   

def player_control(dt):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player_rect.right < settings.SCREEN_WIDTH:
            player_rect.x += settings.SPEED * dt 

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player_rect.left > 0:
            player_rect.x -= settings.SPEED * dt 



def draw_player(screen):
    # pygame.draw.rect(screen, (255,0,0), player_rect, 2) # Displaying the Rect Box
    screen.blit(player, player_rect) # (source, destination)

    
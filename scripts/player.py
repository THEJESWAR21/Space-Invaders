import pygame
import settings


def draw_player(screen):
    player = pygame.image.load("assets/Player.png").convert_alpha() # Load Player Image
    player_rect = player.get_rect() # Gets the Image Rect Position
    player_rect.center = (settings.PLAYER_X, settings.PLAYER_Y)
    
    pygame.draw.rect(screen, (255,0,0), player_rect, 2) # Displaying the Rect Box
    return screen.blit(player, player_rect) # (source, destination)
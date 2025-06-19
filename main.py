import pygame
import sys, os
from scripts.Configs import CONFIG
from scripts.Player import Player

pygame.init()

class Window():
    def __init__(self, ScreenX = CONFIG["X"], ScreenY = CONFIG["Y"]):
        self.X = ScreenX
        self.Y = ScreenY
        self.running = True
        self.Screen = pygame.display.set_mode([self.X, self.Y])
        pygame.display.set_caption(CONFIG["WindowName"])

    def update(self):
        pygame.display.update()
    
    def Quit(self):
        pygame.quit()
        sys.exit()

    def Player(self):
        player_class = Player()
        player = pygame.image.load(player_class.Player_Assets).convert_alpha()
        player_width = player.get_height()
        player_height = player.get_height()
        player = pygame.transform.scale(player_class.Player_Assets, (player_width * 0.4, player.get_height * 0.4))
        self.Screen.blit(player, player_class.player_pos)
        

    def clear_Screen(self):
        self.Screen.fill((0,0,0))

    
def main():
    display = Window()
    clock = pygame.time.Clock()

    while display.running:
        display.clear_Screen()
        display.Player()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.running = False
                display.Quit() 
    
        display.update()
        clock.tick(CONFIG["RefreshRate"])


if __name__ == "__main__":
    main()
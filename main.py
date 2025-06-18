import pygame
import sys, os
from scripts.Configs import CONFIG

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
        Player_Asset = os.path.join("assets", "Player.png")
        player = pygame.image.load(Player_Asset).convert_alpha()
        player_pos = (700, 625)
        player_width = player.get_width()
        player_height = player.get_height()

        player = pygame.transform.scale(player, (player_width * 0.4, player_height * 0.4))
        self.Screen.blit(player, player_pos)

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
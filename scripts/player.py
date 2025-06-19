import pygame
import os

class Player:
    def __init__(self):
        self.Player_Assets = os.path.join("..","assets", "Player.png")
        self.player_pos = (600, 625)
    

    def Player_Movement(self):
        ...
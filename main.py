import pygame

Height = 800
Width = 600


# Player_Size = (60,60)
# Player_Positon = (370,530)

# Pygame Setup
pygame.init()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((Height, Width))
clock = pygame.time.Clock()
running = True

player = pygame.image.load("./assets/Player.png")

while running:
    player = pygame.transform.scale(player, (60,60))
    screen.blit(player, (370,530))



    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
           
    clock.tick(60) # Framerate
pygame.quit()
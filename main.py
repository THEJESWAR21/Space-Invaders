import pygame

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Code Here     

    screen.fill("purple")
    pygame.display.flip()

clock.tick(60) # Framerate
pygame.quit()
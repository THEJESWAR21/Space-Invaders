import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
running = True

Player = pygame.image.load("./assets/Player.png")
Player = pygame.transform.scale(Player, (83.6 , 83.6))

x = 610
y = 625

speed = 500

while running:
    screen.fill((0,0,0))

    dt = clock.tick(60) / 1000.0 
    
    # Player Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed * dt 
    if keys[pygame.K_RIGHT]:
        x += speed * dt


    x = max(0, min(x , 1280 - Player.get_width()))

    screen.blit(Player, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    clock.tick(60)

pygame.quit()

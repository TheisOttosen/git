import pygame
pygame.init()

window = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Snake")

# Spillerens variabler
posX = 50
posY = 50
size = 50
length = 0

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

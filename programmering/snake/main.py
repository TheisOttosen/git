import time # For FPS
import pygame # Pygame import
pygame.init() # Pygame init



window = pygame.display.set_mode((1000,1000)) # Makes the window
pygame.display.set_caption("Snake") # Changes the caption of the game



# Players variables
posX = 50
posY = 50
size = 50
length = 0
PlayerColor = (255,0,0)



# Game variables
BackGroundColor = (0,0,0)
FPS = 30



# Draws everything
def DrawContent():
    pygame.draw.rect(window, BackGroundColor, (0, 0, 1000, 1000)) # Background
    pygame.draw.rect(window, PlayerColor, (posX, posY, size, size)) # Player
    pygame.display.update()
    pass



# Makes the player move
def Movement():
    for event in pygame.event.get():
        if event.type == pygame.K_w:
            posY -= 1
        if event.type == pygame.K_a:
            posY -= 1
        if event.type == pygame.K_s:
            posY -= 1
        if event.type == pygame.K_d:
            posY -= 1
    pass



# Main loop
run = True
while run:
    time.sleep(1/FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Movement()
    DrawContent()

    



pygame.quit()

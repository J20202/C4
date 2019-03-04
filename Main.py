import pygame

pygame.init()

#Pygame Variables
screen = pygame.display.set_mode((800, 600))
done = False

#Game Variables

#Board
# 0 = Empty, 1 = red, 2 = yellow
board = [
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
]



#definitions
def drawBackground():
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 800, 600), 0)





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    drawBackground()
            
            
    pygame.display.flip()

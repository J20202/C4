import pygame

pygame.init()

#Pygame Variables
screen = pygame.display.set_mode((800, 600))
done = False

#Game Variables

#Board





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

import pygame

pygame.init()

# Pygame Variables
screen = pygame.display.set_mode((800, 600))
done = False

# Game Variables

# Mouse Variables


# Board
# 0 = Empty, 1 = red, 2 = yellow
board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]
         ]


# definitions
def drawGame():
    #background
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600), 0)

    #Board
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(50, 50, 700, 500), 0)

    #for a in column1:
    for a in range(0,len(board),1):
        for i in range(0, len(board[a]), 1):
            if board[a][i] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (100 + 100 * i, 100 + 75 * a), 25, 0)
            if board[a][i] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (100 + 100 * i, 100 + 75 * a), 25, 0)
            if board[a][i] == 2:
                pygame.draw.circle(screen, (255, 255, 0), (100 + 100 * i, 100 + 75 * a), 25, 0)

def drawHitBox():
    global mPos

    mPos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for a in range(0,len(board),1):
            for i in range(0, len(board[a]), 1):
                hitBox = pygame.Rect(75 + 100 * i, 75 + 75 * a, 50, 50)
                if hitBox.collidepoint(mPos):
                    board[a][i] = 1

def change





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    drawGame()
    drawHitBox()

    pygame.display.flip()

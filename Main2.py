import pygame

pygame.init()

# Pygame Variables
screen = pygame.display.set_mode((800, 600))
done = False

# Game Variables
# 1 = Red | 2 = Yellow
turn = 1
#time
time = 500

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
    global turn
    global time

    #increases time
    time += 1
    print(time)

    # Sets mPos (Mouse Position) to current xy of mouse.  Stored as (x,y)
    mPos = pygame.mouse.get_pos()
    if time > 500:
        if pygame.mouse.get_pressed()[0]:
            for a in range(0,len(board),1):
                for i in range(0, len(board[a]), 1):
                    hitBox = pygame.Rect(75 + 100 * i, 75 + 75 * a, 50, 50)
                    if hitBox.collidepoint(mPos):
                        board[a][i] = turn
            changeTurn()

def changeTurn():
    global turn
    global time

    time = 0

    if turn == 1: #RED
        turn = 2
    else:
        turn = 1






while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    drawGame()
    drawHitBox()

    pygame.display.flip()

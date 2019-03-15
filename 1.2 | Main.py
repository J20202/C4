import pygame

pygame.init()

# Pygame Variables
screen = pygame.display.set_mode((800, 600))
done = False

# Game Variables
# 1 = Red | 2 = Yellow
turn = 1
col = 0

#time
time = 1000

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
    drawPieces()


def drawPieces():
    #for a in column1:
    for a in range(0,len(board),1):
        for i in range(0, len(board[a]), 1):
            if board[a][i] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (100 + 100 * i, 100 + 75 * a), 25, 0)
            if board[a][i] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (100 + 100 * i, 100 + 75 * a), 25, 0)
            if board[a][i] == 2:
                pygame.draw.circle(screen, (255, 255, 0), (100 + 100 * i, 100 + 75 * a), 25, 0)

def placeGamePiece():
    global col
    global turn

    currentRow = 0
    nextRow = 1

    '''for a in range(0, len(board), 1):
        for i in range(0, len(board[a]), 1):'''
    while board[currentRow][col] == 0:
        if nextRow + 1 > 5:
            board[col][currentRow] = turn
        elif board[nextRow][col] ==0:
            currentRow += 1
            nextRow += 1
        else:
            board[col][nextRow] = turn

def drawHitBox():
    global mPos
    global turn
    global time

    mPos = pygame.mouse.get_pos()
    if time > 1000:
        if pygame.mouse.get_pressed()[0]:
            for a in range(0,len(board),1):
                for i in range(0, len(board[a]), 1):
                    hitBox = pygame.Rect(75 + 100 * i, 75 + 75 * a, 50, 50)
                    if hitBox.collidepoint(mPos):
                        placeGamePiece()
                        print board
                        print col
                        changeTurn()
                        time = 0


def findColumn():
    global mPos
    global col

    if mPos[0] > 75 and mPos[0] <125:
        col = 0
    elif mPos[0] > 175 and mPos[0] < 225:
        col = 1
    elif mPos[0] > 275 and mPos[0] < 325:
        col = 2
    elif mPos[0] > 375 and mPos[0] < 425:
        col = 3
    elif mPos[0] > 475 and mPos[0] < 525:
        col = 4
    elif mPos[0] > 575 and mPos[0] < 625:
        col = 5
    elif mPos[0] > 675 and mPos[0] < 725:
        col = 6


def checkForWin():
    pass

def gravity():
    global col
    global turn






def changeTurn():
    global turn

    if turn == 1: #RED
        turn = 2
    else:
        turn = 1

def incTime():
    global time

    time += 1

def test():
    global mPos

    #if pygame.mouse.get_pressed()[2]:
        #print mPos





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    drawGame()
    drawHitBox()
    incTime()
    findColumn()

    test()
    gravity()

    pygame.display.flip()

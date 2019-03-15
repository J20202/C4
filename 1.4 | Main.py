import pygame

pygame.init()
pygame.font.init()

# Pygame Variables
screenW = 800
screenH = 600
screen = pygame.display.set_mode((screenW, screenH))
done = False
myFont = pygame.font.SysFont('Comic Sans MS', 30)

# Game Variables
# 1 = Red | 2 = Yellow
turn = 1
col = 0
currentCol = 0
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
    global board

    currentRow = 0
    nextRow = 1
    while board[currentRow][col] == 0:
        if nextRow + 1 > 6:
            board[currentRow][col] = turn
        elif board[nextRow][col] == 0:
            currentRow += 1
            nextRow += 1
        else:
            board[currentRow][col] = turn

'Calls two lines of code'

def drawHitBox():
    global mPos
    global turn
    global time
    global currentCol

    mPos = pygame.mouse.get_pos()
    if time > 1000:
        if pygame.mouse.get_pressed()[0]:
            for a in range(0,len(board),1):
                for i in range(0, len(board[a]), 1):
                    hitBox = pygame.Rect(75 + 100 * i, 75 + 75 * a, 50, 50)
                    if hitBox.collidepoint(mPos):
                        placeGamePiece()
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

def winDown(row,col):
    if row + 3 > 5: # out of bounds
        return 0
    current = board[row][col]
    oneDown = board[row + 1][col]
    twoDown = board[row + 2][col]
    threeDown = board[row + 3][col]
    if current == oneDown and current == twoDown and current == threeDown:
        return current
    else:
        return 0

def checkForWin():
    for row in range(0, len(board), 1):
        for col in range(0, len(board[row]), 1):
            resultDown = winDown(row, col)
            #resultRight = winRight(row, col)
            if resultDown == 1:
                print "red won"


def changeTurn():
    global turn
    if turn == 1: #Red
        turn = 2
    else:
        turn = 1

def incTime():
    global time

    time += 1

def displayText():

    if turn == 1:
        textSurface = myFont.render("It is red's turn", False,
                                    (255, 255, 255))
        textSurface_rect = textSurface.get_rect(center=(screenW / 2, 20))
        screen.blit(textSurface, textSurface_rect)
    if turn == 2:
        textSurface = myFont.render("It is yellow's turn", False,
                                    (255, 255, 255))
        textSurface_rect = textSurface.get_rect(center=(screenW / 2, 20))
        screen.blit(textSurface, textSurface_rect)




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    drawGame()
    drawHitBox()
    incTime()
    findColumn()
    displayText()
    checkForWin()

    pygame.display.flip()

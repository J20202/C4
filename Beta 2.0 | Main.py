import pygame

pygame.init()
pygame.font.init()

# Pygame Variables
screenW = 800
screenH = 600
screen = pygame.display.set_mode((screenW, screenH))
done = False
winFont = pygame.font.SysFont('Comic Sans MS', 30)
textFont = pygame.font.SysFont('Comic Sans MS', 20)

# Game Variables
# 1 = Red | 2 = Yellow
turn = 1
col = 0
currentCol = 0
win = 0
# Time
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
    # Background
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600), 0)

    #Board
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(50, 50, 700, 500), 0)
    drawPieces()

def drawPieces():
    for row in range(0,len(board), 1):
        for col in range(0, len(board[row]), 1):
            if board[row][col] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (100 + 100 * col, 100 + 75 * row), 25, 0)
            if board[row][col] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (100 + 100 * col, 100 + 75 * row), 25, 0)
            if board[row][col] == 2:
                pygame.draw.circle(screen, (255, 255, 0), (100 + 100 * col, 100 + 75 * row), 25, 0)

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
    if time > 300:
        if pygame.mouse.get_pressed()[0]:
            for row in range(0,len(board),1):
                for col in range(0, len(board[row]), 1):
                    hitBox = pygame.Rect(75 + 100 * col, 75 + 75 * row, 50, 50)
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
    current = board[row][col]
    oneDown = board[row + 1][col]
    twoDown = board[row + 2][col]
    threeDown = board[row + 3][col]
    
    if row + 3 > 5: # Out of bounds
        return 0
    if current == oneDown == twoDown == threeDown:
        return current
    else:
        return 0

def winRight(row,col):
    current = board[row][col]
    oneRight = board[row][col + 1]
    twoRight = board[row][col + 2]
    threeRight = board[row][col + 3]
    
    if col + 3 > 6: # Out of bounds
        return 0
    if current == oneRight == twoRight == threeRight:
        return current
    else:
        return 0
 
'''def winDiag(row,col):  # Reformat when done
    if col + 3 > 6 and row + 3 > 5:
        return 0
    current = board[row][col]
    oneDiag = board[row - 1][col + 1]
    twoDiag = board[row - 2][col + 2]
    threeDiag = board[row - 3][col + 3]
    if current == oneDiag == twoDiag == threeDiag:
        return current
    else:
        return 0'''

def checkForWin():
    global win

    for row in range(0, len(board), 1):
        for col in range(0, len(board[row]), 1):
            resultDown = winDown(row, col)
            resultRight = winRight(row, col)
            #resultDiag = winDiag(row, col)
            if resultDown == 1:
                win = 1
            elif resultDown == 2:
                win = 2
            if resultRight == 1:
                win = 1
            elif resultRight == 2:
                win = 2
            '''if resultDiag == 1:
                win = 1
            elif resultDiag == 2:
                win = 2'''

def changeTurn():
    global turn
    
    if turn == 1: # Red
        turn = 2
    else:         # Yellow
        turn = 1

def incTime():
    global time

    time += 1

def displayText():
    if turn == 1: # Red's turn
        textSurface = winFont.render("It is red's turn", False, (255, 255, 255))
        textSurface_rect = textSurface.get_rect(center=(screenW / 2, 20))
        screen.blit(textSurface, textSurface_rect)
    elif turn == 2: # Yellow's turn
        textSurface = winFont.render("It is yellow's turn", False, (255, 255, 255))
        textSurface_rect = textSurface.get_rect(center=(screenW / 2, 20))
        screen.blit(textSurface, textSurface_rect)
    if win == 1: # If red wins
        # Displays backsground
        pygame.draw.rect(screen, (50, 50, 50), pygame.Rect((screenW / 2)-200, (screenH / 2)-100, 400, 200), 0)

        # Displays win text
        textWin = winFont.render("Red WINS!", False, (255, 0, 0))
        textWin_rect = textWin.get_rect(center=(screenW / 2, screenH / 2))
        screen.blit(textWin, textWin_rect)

        # Displays restart text
        textSurface = textFont.render("Press Space to restart!", False, (0, 0, 0))
        textSurface_rect = textSurface.get_rect(center=(screenW / 2, (screenH / 2) + 50))
        screen.blit(textSurface, textSurface_rect)

        # Checks for restart
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if win > 0:
                    restartGame()
    elif win == 2: # If Yellow wins
        # Displays background
        pygame.draw.rect(screen, (50, 50, 50), pygame.Rect((screenW / 2) - 200, (screenH / 2) - 100, 400, 200), 0)

        # Displays win text
        textWin = winFont.render("YELLOW WINS!", False, (255, 255, 0))
        textWin_rect = textWin.get_rect(center=(screenW / 2, screenH / 2))
        screen.blit(textWin, textWin_rect)

        # Displays restart text
        textSurface = textFont.render("Press Space to restart!", False, (0, 0, 0))
        textSurface_rect = textSurface.get_rect(center=(screenW / 2, (screenH / 2) + 50))
        screen.blit(textSurface, textSurface_rect)

        # Checks for restart
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if win > 0:
                    restartGame()

def restartGame():
    global board
    global time
    global win
    global turn

    # Resets the bored
    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]
             ]
    # Fixes the rest of the variables
    time = 1000
    win = 0
    turn = 1

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

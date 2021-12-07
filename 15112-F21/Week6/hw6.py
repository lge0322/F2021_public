#################################################
# hw6.py
#
# Your name: Gaeun Lee
# Your andrew id: gaeunl
#
# Your partner's name: Sophia King
# Your partner's andrew id: seking
#################################################

import cs112_f21_week6_linter
import math, copy, random

from cmu_112_graphics import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

import math

def isPerfectSquare(n):
    value = roundHalfUp(math.sqrt(n)) 
    if n == value ** 2:
        return True
    else:
        return False

def isSortOfSquarish(n):
    if n < 0 : return False
    if isPerfectSquare(n): return False #should not be a perfect square
    res = []
    value = 0
    while n > 0:
        onesDigit = n % 10
        if onesDigit == 0:
            return False
        res.append(onesDigit)
        n //= 10
    res.sort() #sort from least to greatest 
    for i in range(len(res)):
        value += res[i] * 10 **((len(res) - (i+1)))
    if isPerfectSquare(value):
        return True
    return False

def nthSortOfSquarish(n):
    current = 0
    found = 0
    value = -1
    while found <= n:
        value += 1
        if isSortOfSquarish(value): 
            found += 1
            current = value
            if value < current:
                found -= 1
    return value

#################################################
# s21-midterm1-animation
#################################################

def s21MidtermAnimation_appStarted(app):
    s21MidtermAnimation_resetApp(app)

def findNearestCircle(app, x, y):
    bestDistance = 99999
    if app.circleCenters != []:
        for circle in app.circleCenters:
            distance = math.floor(math.sqrt((circle[0]-x)**2 
                                                + (circle[1] - y)**2))
            if distance < bestDistance:
                (nearestX, nearestY) = (circle[0], circle[1])
        return (nearestX, nearestY)
    return (x, y)

def s21MidtermAnimation_resetApp(app):
    app.timerDelay = 500
    app.count = 0
    app.circleCenters = []
    app.Lines = []

def s21MidtermAnimation_keyPressed(app, event):
    if event.key == "r": s21MidtermAnimation_resetApp(app)

def s21MidtermAnimation_mousePressed(app, event):
    newCircleCenter = (event.x, event.y)
    app.nearestX, app.nearestY = findNearestCircle(app, event.x, event.y)
    app.circleCenters.append(newCircleCenter)
    
def s21MidtermAnimation_timerFired(app):
    app.count += 10
    if app.count > app.timerDelay:
        s21MidtermAnimation_resetApp(app)

def s21MidtermAnimation_redrawAll(app, canvas):
    (x, y) = (0, 0)
    for circleCenter in app.circleCenters:
        (x, y) = circleCenter
        r = 20
        canvas.create_oval(x-r, y-r, x+r, y+r, fill = 'green')
    if len(app.circleCenters) > 1:
        canvas.create_line(x, y, app.nearestX, app.nearestY, 
                            fill = 'black', width = 2)
        
def s21Midterm1Animation():
    runApp(width=400, height=400, fnPrefix='s21MidtermAnimation_')

#################################################
# Tetris
#################################################

def appStarted(app):
    app.timerDelay = 200
    app.score = 0
    app.gameOver = False
    rows, cols, cellSize, margin = gameDimensions()
    app.rows = rows
    app.cols = cols
    app.cellSize = cellSize
    app.margin = margin
    app.width = app.cols * app.cellSize + app.margin
    app.height = app.rows * app. cellSize + app.margin
    app.emptyColor = "blue"
    app.board = ([[app.emptyColor]*cols for i in range(app.rows)])

 # Seven "standard" pieces (tetrominoes)

    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]

    app.tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    app.tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", 
                                "green", "orange" ]
    newFallingPiece(app)
    
def pointInGrid(app, x, y): #from 112 notes
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def getCell(app, x, y): #from 112 notes
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    # Note: we have to use int() here and not just // because
    # row and col cannot be floats and if any of x, y, app.margin,
    # cellWidth or cellHeight are floats, // would still produce floats.
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)

def gameDimensions():
    rows = 15
    cols = 10
    cellSize = 20
    margin = 25
    return (rows, cols, cellSize, margin)

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, canvas, row, col, app.board[row][col])
            
def drawCell(app, canvas, rows, cols, color): #from cmu 112 websites
    x0, y0, x1, y1 = getCellBounds(app, rows, cols)
    canvas.create_rectangle(x0, y0, x1, y1, fill= color, width = "3" )

def getCellBounds(app, row, col): #from cmu 15112 website
    gridWidth  = app.width - 2 * app.margin
    gridHeight = app.height - 2 * app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col + 1) / app.cols
    y0 = app.margin + gridHeight * row / app.rows
    y1 = app.margin + gridHeight * (row + 1) / app.rows
    return (x0, y0, x1, y1)

def keyPressed(app, event):
    if event.key == 'Left': moveFallingPiece(app, 0, -1)
    elif event.key == 'Right': moveFallingPiece(app, 0, 1)
    elif event.key == 'Up': rotateFallingPiece(app)
    elif event.key == 'Down': moveFallingPiece(app, 1, 0)
    elif event.key == 'r': appStarted(app)
    elif event.key == 'Space': hardDrop(app)

def rotateFallingPiece(app):
    newRows = len(app.fallingPiece[0])
    newCols = len(app.fallingPiece)
    res = new2DList(newRows, newCols)
    for row in range(len(app.fallingPiece)): 
        for col in range(len(app.fallingPiece[0])): 
            nrow = len(app.fallingPiece[0]) - col -1
            ncol = row
            res[nrow][ncol] = app.fallingPiece[row][col]

    newFallingPieceRow = app.fallingPieceRow + newCols//2 - newRows//2
    newFallingPieceCol = app.fallingPieceCol + newRows//2 - newCols//2
    #set new values
    app.fallingPiece = res
    app.fallingPieceRow = newFallingPieceRow
    app.fallingPieceCol = newFallingPieceCol

    if not fallingPieceIsLegal(app):
        app.fallingPiece = app.fallingPiece
        app.fallingPieceRow = len(app.fallingPiece)
        app.fallingPieceCol = len(app.fallingPiece[0])

def newFallingPiece(app):
    import random
    randomIndex = random.randint(0, len(app.tetrisPieces) -1)
    app.fallingPiece = app.tetrisPieces[randomIndex]
    app.fallingPieceColor = app.tetrisPieceColors[randomIndex]
    app.fallingPieceRow = 0
    app.fallingPieceCol = app.cols // 2 - len(app.fallingPiece[0]) // 2 

def drawFallingPiece(app, canvas):
    for i in range(len(app.fallingPiece)):
        for j in range(len(app.fallingPiece[0])):
            if app.fallingPiece[i][j]: #should be the location in fallingPiece
                drawCell(app, canvas, app.fallingPieceRow+i, 
                            app.fallingPieceCol+j, app.fallingPieceColor)

def moveFallingPiece(app, drow, dcol):
    app.fallingPieceRow += drow
    app.fallingPieceCol += dcol
    if not fallingPieceIsLegal(app):
        app.fallingPieceRow -= drow
        app.fallingPieceCol -= dcol
        return False
    return True

def fallingPieceIsLegal(app):
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            if app.fallingPiece[row][col]:
                newRow = app.fallingPieceRow + row
                newCol = app.fallingPieceCol + col
                if (((newRow < 0) or (newRow >= app.rows)) or 
                    ((newCol < 0) or (newCol >= app.cols)) or 
                        app.board[newRow][newCol] != app.emptyColor):
                    return False
    return True

def timerFired(app):
    if app.gameOver: return
    if not moveFallingPiece(app, 1, 0): #should go downwards
        placeFallingPiece(app)
        newFallingPiece(app)
    if not fallingPieceIsLegal(app): 
        app.gameOver = True

def placeFallingPiece(app):
    for i in range(len(app.fallingPiece)):
        for j in range(len(app.fallingPiece[0])):
            if app.fallingPiece[i][j]: 
                row = app.fallingPieceRow +i
                col = app.fallingPieceCol +j
                app.board[row][col] = app.fallingPieceColor
    removeFullRows(app)

def removeFullRows(app):
    count = 0
    for row in range(app.rows):
        if app.board[row].count(app.emptyColor) == 0:
                app.board.pop(row)
                app.board.insert(0, [app.emptyColor]*app.cols)
                count += 1
    app.score = app.score + (count ** 2)

def drawScore(app, canvas):
    canvas.create_text(app.width/2, app.height/30, 
                        text = f'current score: {app.score}',
                        font = 'Arial 15 bold', fill = 'black')
def hardDrop(app):
    if fallingPieceIsLegal(app): #for fallingPiece
        if moveFallingPiece(app, 1, 0) == False: placeFallingPiece(app)
        
def new2DList(rows, cols): #from 112 website
    return [([None]*cols) for row in range(rows)]

def playTetris(app): 
    runApp(width = app.width, height = app.height)

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "orange")
    drawBoard(app, canvas)
    drawFallingPiece(app, canvas)
    drawScore(app, canvas)
    if app.gameOver:
        canvas.create_text(app.width /2 , app.height/2 - app.height/10, 
                            text="Game Over!",
                            fill = 'white', font = 'Arial 36')
        canvas.create_text(app.width/2,app.height/2 + app.height/10, 
                            text="press 'r' to restart the game",
                            fill = 'white', font = 'Arial 24')

def playTetris():
    runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare(n))...', end='')
    assert(isPerfectSquare(4) == True)
    assert(isPerfectSquare(9) == True)
    assert(isPerfectSquare(10) == False)
    assert(isPerfectSquare(225) == True)
    assert(isPerfectSquare(1225) == True)
    assert(isPerfectSquare(1226) == False)
    print('Passed')


def testIsSortOfSquarish():
    print('Testing isSortOfSquarish(n))...', end='')
    assert(isSortOfSquarish(52) == True)
    assert(isSortOfSquarish(252) == True)
    assert(isSortOfSquarish(16) == False)
    assert(isSortOfSquarish(502) == False)
    assert(isSortOfSquarish(414) == True)
    assert(isSortOfSquarish(5221) == True)
    assert(isSortOfSquarish(6221) == False)
    assert(isSortOfSquarish(-52) == False)
    print('Passed')


def testNthSortOfSquarish():
    print('Testing nthSortOfSquarish()...', end='')
    assert(nthSortOfSquarish(0) == 52)
    assert(nthSortOfSquarish(1) == 61)
    assert(nthSortOfSquarish(2) == 63)
    assert(nthSortOfSquarish(3) == 94)
    assert(nthSortOfSquarish(4) == 252)
    assert(nthSortOfSquarish(8) == 522)
    print('Passed')

def testAll():
    testIsPerfectSquare()
    testIsSortOfSquarish()
    testNthSortOfSquarish()

#################################################
# main
#################################################

def main():
    cs112_f21_week6_linter.lint()
    s21Midterm1Animation()
    playTetris()
    testAll()

if __name__ == '__main__':
    main()

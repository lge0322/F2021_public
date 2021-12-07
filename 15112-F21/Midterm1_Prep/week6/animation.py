from cmu_112_graphics import *
import time


def bob_appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 15
    app.bobrow = 0
    app.bobcol = 0
    app.bobradius = (app.width - 2 *app.margin) / app.cols // 2
    app.bobLives = 3
    app.initialTime = time.time()

def moveBob(app, drow, dcol):
    app.bobrow += drow
    app.bobcol += dcol
    if (app.bobrow < 0 or app.bobcow >= app.rows or app.bobcol < 0   or 
        app.bobcol >= app.cols):
        app.bobrow -= drow
        app.bobcol -= dcol

def bob_timerFireD(app):
    currTime = time.time()
    elapsedTime = currTime - app.initialTime
    if elapsedTime > 2:
        app.bobLives += 1
        app.initialTime = currTime


def bob_keyPressed(app, event):
    if event.key == "Right":
        moveBob(app, 0, 1)
    elif event.key == "Left":
        app.bobcol -= 1
    elif event.key == "Up":
        app.bobrow -= 1
    elif event.key == "Down":
        app.bobrow += 1

def drawGrid(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)
    
def getCellBounds(app, row, col):
    cellWidth = (app.width - 2*app.margin)/ app.cols
    cellHeight = (app.height - 2*app.margin)/ app.rows
    x0 = cellWidth * col + app.margin
    x1 = cellWidth * (col+1) 
    y0 = cellHeight * row + app.margin
    y1 = cellHeight * (row+1)
    return x0, x1, y0, y1

def drawBob(app, canvas):
    x0, y0, x1, y1 = getCellBounds(app, app.bobrow, app.bobcol)
    canvas.create_oval(x0, y0, x1, y1, fill = 'magenta')

def redrawAll(app, canvas):
    drawGrid(app, canvas)
    drawBob(app, canvas)
from dataclasses import make_dataclass
import math

Circle = make_dataclass('Circle', ['cx', 'cy', 'r', 'color', 'speed'])
def appStarted(app):
    app.maxR = min(app.height, app.width / 2)
    app.smallCircle = Circle(cx = 0, cy = app.height/2, r = 10, color = 'black',
                               speed = 10)

    app.sink = Circle(cx = app.width, cy = app.height/2, r=5, color = 'red', 
                        speed =5)

def drawCircle(circle, canvas):
    canvas.create_oval(circle.cx - circle.r, circle.cy - circle.r,
                        circle.cx + circle.r, circle.cy + circle.r,
                            color = circle.color)

def redrawAll(app, canvas):
    drawCircle(app.smallCircle, canvas)
    drawCircle(app.sink, canvas)





runApp(width = 400, height = 400)

def appStarted(app):
    app.circleCenters = []

def mousePressed(app, event):
    newCircleCenter = (event.x, event.y)
    if len(app.circleCenters) > 0:
        app.circleCenters.pop(0)
    else:
        print('No more')

def redrawAll(app, canvas):
    for circleCenter in app.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = 'cyan')
    
runApp (width = 400, height = 400)
def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 40

def keyPressed(app, event):
    if (event.key == 'Left'):
        app.cx -= 10
        if (app.cx - app.r < 0):
            app.cx = app.width + app.r
    elif (event.key == 'Right'):
        app.cx += 10
        if (app.cx + app.r > app.width):
            app.cx = 0 - app.r

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 20, text = 'Move dot with left and right')
    canvas.create_oval(app.cx-app.r, app.cy-app.r, 
                        app.cx+app.r, app.cy+app.r, fill = 'darkGreen')
runApp(width=400, height=400)


from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 40

def mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 20,
                       text='Move dot with mouse presses')
    canvas.create_oval(app.cx-app.r, app.cy-app.r,
                       app.cx+app.r, app.cy+app.r,
                       fill='darkGreen')

runApp(width=400, height=400)


from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 40

def timerFired(app):
    app.cx -= 10
    if (app.cx + app.r <= 0):
        app.cx = app.width + app.r

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 20,
                       text='Watch the dot move!')
    canvas.create_oval(app.cx-app.r, app.cy-app.r,
                       app.cx+app.r, app.cy+app.r,
                       fill='darkGreen')

runApp(width=400, height=400)

from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 40
    app.paused = False

def timerFired(app):
    if (not app.paused):
        doStep(app)

def doStep(app):
    app.cx -= 10
    if (app.cx + app.r <= 0):
        app.cx = app.width + app.r

def keyPressed(app, event):
    if (event.key == 'p'):
        app.paused = not app.paused
    elif (event.key == 's') and app.paused:
        doStep(app)

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 20,
                       text='Watch the dot move!')
    canvas.create_text(app.width/2, 40,
                       text='Press p to pause or unpause')
    canvas.create_text(app.width/2, 60,
                       text='Press s to step while paused')
    canvas.create_oval(app.cx-app.r, app.cy-app.r,
                       app.cx+app.r, app.cy+app.r,
                       fill='darkGreen')

runApp(width=400, height=400)

from cmu_112_graphics import *

def appStarted(app):
    app.rows = 4
    app.cols = 8
    app.margin = 5 # margin around grid
    app.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none

def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def getCell(app, x, y):
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

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

def mousePressed(app, event):
    (row, col) = getCell(app, event.x, event.y)
    # select this (row, col) unless it is selected
    if (app.selection == (row, col)):
        app.selection = (-1, -1)
    else:
        app.selection = (row, col)

def redrawAll(app, canvas):
    # draw grid of cells
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "orange" if (app.selection == (row, col)) else "cyan"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    canvas.create_text(app.width/2, app.height/2 - 15, text="Click in cells!",
                       font="Arial 26 bold", fill="darkBlue")

runApp(width=400, height=400)



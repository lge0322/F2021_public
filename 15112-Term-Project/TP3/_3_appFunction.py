from _1_classes import *
from _2_createImage import *


################################################################################

def reset(app):
    createImage(app)

    app.margin = min(app.height, app.width) // 10
    app.minMargin = app.margin // 5
    app.level = 1
    app.level1= True
    app.level2 = False
    app.level3 = False
    app.wallList = [] #shows the location of the walls format: (x,y)
    app.color = "red"
    app.rows, app.cols = maze1.rows, maze1.cols
    app.w = maze1.w
    app.speed = 0
    app.gameOver = False
    app.status = "Closed"
    app.numCoin = 5
    app.doorOpen = False
    app.charAtDoor = False
    app.isNext = False

    app.hintButton = False

    if woodboy.die or metalgirl.die:
        app.gameOver = True

    app.coinLocation = []


################################################################################

def charAtDoor(app):
    if app.doorOpen:
        if ((woodboy.x - app.minMargin  <= woodboy.initX <= woodboy.x + app.minMargin and
            woodboy.y - app.minMargin  <= woodboy.initY <= woodboy.y + app.minMargin) and 
            (metalgirl.x -app.minMargin  <= metalgirl.initX <= metalgirl.x + app.minMargin and 
            metalgirl.y - app.minMargin  <= metalgirl.initY <= metalgirl.y + app.minMargin)):
            app.isNext = True


################################################################################
from temp import *

from cmu_112_graphics import *
from _2_createImage import *

import random


#initalize values

def reset(app):
    createImage(app)

    app.pause = False 
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

    if woodboy.die or metalgirl.die:
        app.gameOver = True

    app.coinLocation = []


def appStarted(app): 
    reset(app)

def charAtDoor(app):
    if app.doorOpen:
        print('finally')
        if ((woodboy.x - app.minMargin  <= woodboy.initX <= woodboy.x + app.minMargin and
            woodboy.y - app.minMargin  <= woodboy.initY <= woodboy.y + app.minMargin) and 
            (metalgirl.x -app.minMargin  <= metalgirl.initX <= metalgirl.x + app.minMargin and 
            metalgirl.y - app.minMargin  <= metalgirl.initY <= metalgirl.y + app.minMargin)):
            app.isNext = True


def keyPressed(app, event):
    if app.gameOver:
        return
    
    if event.key == "r":
       pass

    if event.key == "Right":
        woodboy.x += woodboy.speed
        #woodboy.speed += 1
    elif event.key == "Left":
        woodboy.x -= woodboy.speed
        #woodboy.speed += 1
    elif event.key == "Up":
        woodboy.y -= woodboy.speed
        #woodboy.speed += 1
    elif event.key == "Down":
        woodboy.y += woodboy.speed
        #woodboy.speed += 1
    
    if event.key == "d":
        metalgirl.x += metalgirl.speed
        #metalgirl.speed += 1
    elif event.key == "a":
        metalgirl.x -= metalgirl.speed
        #metalgirl.speed += 1
    elif event.key == "w":
        metalgirl.y -= metalgirl.speed
        #metalgirl.speed += 1
    elif event.key == "s":
        metalgirl.y += metalgirl.speed
        #metalgirl.speed += 1


##revisit from here!!!!!w = maze1.w


def timerFired(app):

    charAtDoor(app)

    #if woodboy.die or metalgirl.die:
      #  app.gameOver = True
    

    #should be "sums"
    if app.level1:
        maze1.check(app)
        maze1.consumed(app)
    if app.level2:
        maze2.check(app)
        maze2.consumed(app)

    #consume coins 

  

   
def drawSetup(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image = app.background) #hardcode
    canvas.create_rectangle(0, 0, 400, 400, fill = "yellow")

    canvas.create_text(470, 40, text = f'level {app.level}', fill = "black", font = "Arial 15 bold")


    #indicating the status of the door (whether it is open or not)

    canvas.create_text(490, 520, text = f'{app.status}', fill = app.color, font = "Arial 16 bold")




def drawCharacters(app, canvas):
    canvas.create_image(woodboy.x, woodboy.y, image = app.woodboy)
    canvas.create_image(metalgirl.x, metalgirl.y, image = app.metalgirl)

def drawObstacleMove(app, canvas):
    lightning1.draw(app, canvas)
    lightning1.move()
    lightning1.isCharacterTouching()
    lightning2.draw(app, canvas)
    lightning2.move()
    lightning2.isCharacterTouching()
    lightning3.draw(app, canvas)
    lightning3.move()
    lightning3.isCharacterTouching()
    waterdrop1.draw(app, canvas)
    waterdrop1.move()
    waterdrop1.isCharacterTouching()
    waterdrop2.draw(app, canvas)
    waterdrop2.move()
    waterdrop2.isCharacterTouching()
    waterdrop3.draw(app, canvas)
    waterdrop3.move()
    waterdrop3.isCharacterTouching()

def drawGameOver(app, canvas):
    if woodboy.die or metalgirl.die:
            canvas.create_text(200, 200, text = "Try again!", font = "Arial 20 bold")


def mousePressed(app, event):
    r = 40
    if 100 - r < event.x <= 100 +r and 100-r < event.y <= 100+r:
        app.level1 = True
        app.isNext = False
    elif 200 -r < event.x <= 200+r and 200 -r < event.y <= 200+r:
        app.level2 = True
        app.isNext = False
    elif 300 -r < event.x <= 300+r and 300 -r < event.y <= 300+r:
        app.level3 = True
        app.isNext = False
    
    
def redrawAll(app, canvas):
        if app.isNext:
            if app.level1:
                drawSetup(app, canvas)
                maze1.allDraw(app, canvas)
                drawAll(app, canvas)

            elif app.level2:
                drawSetup(app, canvas)
                maze2.allDraw(app, canvas)
                drawAll(app, canvas)
        else:
                drawSetup(app, canvas)
                maze1.allDraw(app, canvas)
                drawAll(app, canvas)
            
            

def drawAll(app, canvas):
    
    drawCharacters(app, canvas)
          #allows lightning and waterdrops move
    drawObstacleMove(app, canvas)

    drawGameOver(app, canvas)

runApp(width = 550, height = 550)

from _1_classes import *
from _2_createImage import *
from _3_appFunction import *

import time

def drawAll(app, canvas):
    
    drawSetup(app, canvas)
    drawInstructions(app, canvas)
    draw1MazeSetup(app, canvas)
    drawCharacters(app, canvas)
    drawHint(app, canvas)
    #drawLift(app, canvas)
    drawSwitch(app, canvas)
    drawCoins(app, canvas)

    hangingwood1.draw(app, canvas)
    button.draw(app, canvas)
    
    #allows lightning and waterdrops move
    drawObstacleMove(app, canvas)
    


    if not len(maze1.hintList) == 0:
        canvas.create_text(470, 330, text = "you have only one hint!" , font = "Arial 12 bold", fill = "black")

    if not len(maze1.hintList) == 0 and app.hintButton:

        drawSolve(app, canvas)


################################################################################

def drawSetup(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image = app.background) #hardcode
    canvas.create_rectangle(0, 0, 400, 400, fill = "yellow")

    canvas.create_text(470, 40, text = f'level {app.level}', fill = "black", font = "Arial 15 bold")


################################################################################

def drawInstructions(app, canvas):

    #indicating # of gems to users

    canvas.create_rectangle(410, 60, 540, 300, fill = "white", outline = "yellow")
    if maze1.counter == sums:
        canvas.create_text(470, 100, text = f'All coins are \n collected!', fill = "red", font = "Arial 13 bold")
    else:
        canvas.create_text(470, 100, text = f'Currently,\n {maze1.counter}\n coins \n are consumed', fill = "black", font = "Arial 13 bold")
    
    #indicating whether switches are open or not
    if switch.isRight:
            canvas.create_text(470, 180, text = f'The switch \n has been \n open!', font = "Arial 13 bold", fill = "red")
        
    else:
            canvas.create_text(470, 180, text = f'Currently, \n the switch \n is not open', fill = "black", font = "Arial 13 bold")
    
    if button.isPressed:
        canvas.create_text(470, 250, text = "The button\n has been\n pressed!", font = "Arial 13 bold", fill = "red")
    else:
        canvas.create_text(470,250, text = "The button\n has not been\n pressed.", font = "Arial 13 bold")
    #indicating the status of the door (whether it is open or not)

    canvas.create_text(490, 520, text = f'{app.status}', fill = app.color, font = "Arial 16 bold")

################################################################################

def drawHint(app, canvas):
    canvas.create_rectangle(420, 350, 520, 400, fill = "white", outline = "yellow")
    canvas.create_text(470, 375, text = "Show Hint", font = "Arial 12 bold")


################################################################################

def draw1MazeSetup(app, canvas):
    maze1.draw(canvas)
    maze1.drawDoor(app, canvas)
    maze1.isWallwithCharacter() #check if the characters are collding with the wall


################################################################################

def drawLift(app, canvas):
    for j in range(len(maze1.liftLoc)):
            w = app.w
            r = w/2
            x, y = maze1.liftLoc[j][0] * w + r, maze1.liftLoc[j][1] * w
            canvas.create_image(x, y+app.speed, image = app.lift)


################################################################################

def drawSwitch(app, canvas):
    switch.draw(app, canvas)


################################################################################

def drawCharacters(app, canvas):
    canvas.create_image(woodboy.x, woodboy.y, image = app.woodboy)
    canvas.create_image(metalgirl.x, metalgirl.y, image = app.metalgirl)


################################################################################


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


################################################################################



################################################################################
random.shuffle(maze1.gem)
res = []
sums = 0
w=  maze1.w
r = w/2
d = r/2
for i in range(3):

    (x, y) = maze1.gem[i][0] * w + r, maze1.gem[i][1] * w +r
    sums+= 1
    res.append((x, y))
    maze1.gem.remove((maze1.gem[i][0], maze1.gem[i][1]))

resG = []
for i in range(3, 6):
    (x, y) = maze1.gem[i][0] * w + r, maze1.gem[i][1] * w +r
    sums += 1
    resG.append((x, y))
    maze1.gem.remove((maze1.gem[i][0], maze1.gem[i][1]))

resB = []

for i in range(6, 8):
    if len(maze1.canBeLift()) == 0:
        break
    (x, y) = maze1.gem[i][0] * w + r, maze1.gem[i][1] * w +r
    sums += 1
    resB.append((x, y))

    
        
def drawCoins(app, canvas):
    for (x, y) in res: #revisit (increase the number of coins)
        coin = canvas.create_image(x, y, image = app.coin)
    if switch.isRight:
        for (x, y) in resB:
            canvas.create_image(x, y, image = app.coinB)
    if button.isPressed:
            for (x, y) in resG:
                canvas.create_image(x, y, image = app.coinG)


################################################################################

def drawGameOver(app, canvas):
    if woodboy.die or metalgirl.die:
        canvas.create_rectangle(0, 100, 400, 300, fill = "white", outline = "gray")
        if woodboy.hitByWaterdrop:
            canvas.create_text(200, 200, text = "Try again!\n Woodboy is hit by waterdrops\n Press 'r' to restart the entire game", font = "Arial 20 bold")
        elif metalgirl.hitByLightning:
            canvas.create_text(200, 200, text = "Try again!\n Metalgirl is hit by lightning\n Press 'r' to restart the entire game", font = "Arial 20 bold")

        elif woodboy.wall or metalgirl.wall:
            canvas.create_text(200, 200, text = "Try again!\n You are hit by the wall\n Press 'r' to restart the entire game ", font = "Arial 20 bold")


################################################################################
        
def drawSolve(app, canvas):
    current = maze1.hintList.pop()
    x,y,dic = current.x, current.y, current.walls
    x = x*maze1.w
    y = y*maze1.w
    r = maze1.w//2
    midX = x + r
    midY = y + r
    d = r// 5
     
    canvas.create_rectangle(midX - d, midY-d, midX+d, midY+d, fill = "green")
    time.sleep(0.4)

################################################################################

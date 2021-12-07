'''
error: sometimes lift does not have a location, I've put None for resolving the error
but it seems not working. Check the main function

error: characters cannot consume gems. check the function

error: dropping obstacles' velocity increases when characters are moving

error: values of r and w should change according to the difficulties of the levels

things to do:

#when the lifts come down all the way down, gold appear on top of the lift
#when click the button, water disappears
#when done with everything, now finally stars appear in front of the doors,
and characters need to eat them

#for hint:
    I can put a timer on the side of the game for the user
    #if a certain time has passed, I can show the users where to 공략 by
    circling around the object. 




#now move on to the level generation
    #if all the gems are consumed
    (Nov 21st: for now, I would say 3 coins are eaten, doors are open)

6. place water

#draw a platform, yet all the elements are embedded in the random map generation

allows users to select the level
 **I need to implement level generation

 #when level goes up, more waterdrops and more lightning
 #more rows and cols with smaller w
 it should do it

 --> hangingwood
 --> when lift interacts with character, it moves all of them simultaneously

'''

import random

from cmu_112_graphics import *

from _1_classes import *
from _2_createImage import *
from level_generation import *

#initalize values

def appStarted(app): 

    createImage(app)

    app.wallList = [] #shows the location of the walls format: (x,y)

    app.speed = 5
    app.gameOver = False
    app.status = "Closed"
    app.counter = 0

    if woodboy.die or metalgirl.die:
        app.gameOver = True

    app.coinLocation = []

def keyPressed(app, event):
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


def obstacleMove(app, canvas):
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

def timerFired(app):

        if switch.isRight:
                app.speed += 5
        else:
                app.speed -= 5

##revisit from here!!!!!



        



random.shuffle(maze1.gem)

def redrawAll(app, canvas):
        canvas.create_image(200, 200, 
                            image = app.background) #hardcode
        canvas.create_rectangle(0, 0, 400, 400, fill = "yellow")
        canvas.create_text(470, 50, text = f'Currently,\n {maze1.counter} coins \n are consumed', fill = "black", font = "Arial 12 bold")
        canvas.create_text(470, 160, text = f'Currently, \n not all switches \nare open', fill = "black", font = "Arial 13 bold")
        
        canvas.create_text(470, 100, text = f'{maze1.status}', fill = "red", font = "Arial 16 bold")
        canvas.create_text(470, 120, text = f'{maze1.status}', fill = "green", font = "Arial 16 bold")
        maze1.draw(canvas)
        maze1.drawDoor(app, canvas)
        
        
        for i in range(len(maze1.gem)-7 ): #revisit (increase the number of coins)
            w = maze1.w
            r = w/2
            (x, y) = maze1.gem[i][0] * w + r, maze1.gem[i][1] * w +r
            maze1.gemConsumed.append((x,y))
            canvas.create_image(x, y, image = app.coin)
        

        for j in range(len(maze1.liftLoc)):
            w = maze1.w
            r = w/2
            x, y = maze1.liftLoc[j][0] * w + r, maze1.liftLoc[j][1] * w + maze1.speed
            canvas.create_image(x, y, image = app.lift)
            
        
        canvas.create_image(woodboy.x, woodboy.y, image = app.woodboy)
        canvas.create_image(metalgirl.x, metalgirl.y, image = app.metalgirl)
        maze1.isWallwithCharacter()
        switch.draw(app, canvas)

        hangingwood1.draw(app, canvas)
        button.draw(app, canvas)

        obstacleMove(app, canvas)
        #block1.drawBlock(app, canvas)

        if woodboy.die or metalgirl.die:
            canvas.create_text(200, 200, text = "Try again!", font = "Arial 20 bold")
            return

print(maze1.liftLoc)

runApp(width = 550, height = 550)

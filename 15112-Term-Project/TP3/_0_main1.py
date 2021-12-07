import module_manager
module_manager.review()

from cmu_112_graphics import *

from _1_classes import *
from _2_createImage import *
from _3_appFunction import *
from _4_drawFunction import *



###############################################################################
#initalize values

def appStarted(app): 
    app.start = False
    app.main = False

    reset(app)

def keyPressed(app, event):
    
    #for starting page
    if not app.main:
        if event.key:
            app.main = True

    if app.gameOver:
        if event.key == "r":
            app.gameOver = False
            woodboy.die = False
            woodboy.x, woodboy.y = woodboy.initX, woodboy.initY
            metalgirl.x, metalgirl.y = metalgirl.initX, metalgirl.initY
            metalgirl.die = False

            runApp(width = 550, height = 550)
            


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

def timerFired(app):

    charAtDoor(app)

    if woodboy.die or metalgirl.die:
        app.gameOver = True
    
    #should be "sums"
    if maze1.counter == sums: #hardcode
        app.status = "Open"
        app.color = "green"
        app.doorOpen = True

    #consume coins 

    for (x, y) in res:
        if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d) or 
            (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d)):
            maze1.counter += 1
            res.remove((x,y))

    for (x, y) in resG:
        if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d and button.isPressed) or 
            (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d and button.isPressed)):
            maze1.counter += 1
            resG.remove((x,y))

    for (x, y) in resB:
        if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d and switch.isRight) or 
            (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d and switch.isRight)):
            maze1.counter += 1
            resB.remove((x,y))


    for j in range(len(maze1.liftLoc)):
            w = app.w
            r = w/2
            x, y = maze1.liftLoc[j][0] * w + r, maze1.liftLoc[j][1] * w

            if switch.isRight:
                if y <= maze1.liftLoc[j][1] + 2 * w:
                    app.speed += 5
    
            elif switch.touched and not switch.isRight:
                app.speed -= 5
            
            elif not switch.touched and not switch.isRight:
                pass

def mousePressed(app, event):
    
    if app.main and not app.start:
        if 0 <= event.x <= 400 and 0 <= event.y <=400:
            app.start = True

    else:   
        if 450 <= event.x <= 500 and 350 <= event.y <=450:
            app.hintButton = True


#right before the game starts, 
def redrawAll(app, canvas):
    if not app.main and not app.start:
        canvas.create_rectangle(0, 0, 400, 400, fill = "yellow", outline = "black", width = 5)
        canvas.create_rectangle(40, 20, 390, 160, fill = "white", outline = "green")
        canvas.create_text(210, 90, text = "WOODBOY AND METALGIRL", font = "Arial 24 bold")
        canvas.create_rectangle(40, 185, 390, 215, fill = "white", outline = "green")
        canvas.create_text(200, 200, text = "Press any key to start", font = "Arial 13 bold")
        canvas.create_rectangle(40, 350, 390, 380, fill = "white", outline = "green")
        canvas.create_text(200, 365, text = "By Ella Lee", font = "Arial 13 bold")

        
    elif app.main and not app.start:

        canvas.create_rectangle(0, 0, 400, 400, fill = "yellow", outline = "black", width = 5)
        canvas.create_rectangle(40, 20, 390, 160, fill = "white", outline = "green")
        canvas.create_text(210, 90, text = "Instructions", font = "Arial 30 bold")
        canvas.create_rectangle(40, 190, 390, 210, fill = "white", outline = "green")
        canvas.create_text(200, 200, text= "Press one of the characters to get started", font = "Arial 12 bold")
        canvas.create_rectangle(40, 230, 390, 380, fill = "white", outline = "green")
        canvas.create_text(220, 300, text = "Each game will have a randomly generated map. \n\n Rule 1: Do not collide with the wall \n  Rule 2: Woodboy cannot touch waterdrops \n  Rule 3: Metalgirl cannot tough lightning \n  Rule 4: Get all the coins to open the door \n  Rule 5: If the doors are open, go in front of the doors then you win!",
                            font = "Arial 10 bold")
        canvas.create_image(100, 150, image = app.woodboy)
        canvas.create_image(300, 150, image = app.metalgirl)

    elif app.main and app.start:

        if not app.gameOver:

            drawAll(app, canvas)
            if app.isNext:
                canvas.create_rectangle(0, 100, 400, 300, fill = "white", outline = "gray")
                canvas.create_text(200, 200, text = "Yay! You got all the coins!\n Run this app again \nto try another game", font = "Arial 23 bold")
        else:
             drawGameOver(app, canvas)
            

runApp(width = 550, height = 550)

'''

pathfinding --> adding difficulties later

--> structure / strengthen the path finding algorithm

pathfinding // hint system (showing where doors and buttons and switches are)

error: dropping obstacles' velocity increases when characters are moving

error: values of r and w should change according to the difficulties of the levels

things to do:

#when the lifts come down all the way down, gold appear on top of the lift
#when click the button, water disappears
#when done with everything, now finally stars appear in front of the doors,
and characters need to eat them


 #when level goes up, more waterdrops and more lightning
 #more rows and cols with smaller w

 --> hangingwood
 --> when lift interacts with character, it moves all of them simultaneously

'''
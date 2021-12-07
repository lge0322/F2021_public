
from cmu_112_graphics import *

def createImage(app):

    backgroundImage = app.loadImage("backgroundImage.jpg")
    backgroundImage = app.scaleImage(backgroundImage, 1.3)
    app.background = ImageTk.PhotoImage(backgroundImage)

    doorImage = app.loadImage("DoorClosed.png")
    doorImage = app.scaleImage(doorImage, 0.2)
    app.door = ImageTk.PhotoImage(doorImage)

    woodboyImage = app.loadImage("Woodboy.png")
    woodboyImage = app.scaleImage(woodboyImage, 0.08)
    app.woodboy = ImageTk.PhotoImage(woodboyImage)

    metalgirlImage = app.loadImage("Metalgirl.png")
    metalgirlImage = app.scaleImage(metalgirlImage, 0.08)
    app.metalgirl = ImageTk.PhotoImage(metalgirlImage)

    switchLeftImage = app.loadImage("SwitchLeft.png")
    switchLeftImage = app.scaleImage(switchLeftImage, 0.05) #0.08 previously
    app.switchLeft = ImageTk.PhotoImage(switchLeftImage)

    switchRightImage = app.loadImage("SwitchRight.png")
    switchRightImage = app.scaleImage(switchRightImage, 0.05)
    app.switchRight = ImageTk.PhotoImage(switchRightImage)

    buttonImage = app.loadImage("Button.png")
    buttonImage = app.scaleImage(buttonImage, 0.1)
    app.button = ImageTk.PhotoImage(buttonImage)

    waterdropImage = app.loadImage("Waterdrop.png")
    waterdropImage = app.scaleImage(waterdropImage, 0.03)
    app.waterdrop = ImageTk.PhotoImage(waterdropImage)

    lightning1Image = app.loadImage("Lightning1.png")
    lightning1Image = app.scaleImage(lightning1Image, 0.03)
    app.lightning1 = ImageTk.PhotoImage(lightning1Image)

    lightning2Image = app.loadImage("Lightning2.png")
    lightning2Image = app.scaleImage(lightning2Image, 0.03)
    app.lightning2 = ImageTk.PhotoImage(lightning2Image)

    lightning3Image = app.loadImage("Lightning3.png")
    lightning3Image = app.scaleImage(lightning3Image, 0.03)
    app.lightning3 = ImageTk.PhotoImage(lightning3Image)

    liftImage = app.loadImage("Lift.png")
    liftImage = app.scaleImage(liftImage, 0.05) #0.05 previously
    app.lift = ImageTk.PhotoImage(liftImage)

    hangingWoodImage = app.loadImage("HangingWood.png")
    hangingWoodImage = app.scaleImage(hangingWoodImage, 0.15)
    app.hangingWood = ImageTk.PhotoImage(hangingWoodImage)


    coinImage = app.loadImage("Coin.png")
    coinImage = app.scaleImage(coinImage, 0.05)
    app.coin = ImageTk.PhotoImage(coinImage)

'''
coinx.draw(app, canvas)
    coin2.draw(app, canvas)
        coin3.draw(app, canvas)
        coin4.draw(app, canvas)
        coin5.draw(app, canvas)

        coin1.consume(canvas)
        coin2.consume(canvas)
        coin3.consume(canvas)
        '''
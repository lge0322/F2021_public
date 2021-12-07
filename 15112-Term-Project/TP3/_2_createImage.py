
from cmu_112_graphics import *

from _1_classes import *

scale = 0
if maze1.rows == 5:
    scale = 0.1

def createImage(app):

    titleImage = app.loadImage("Title.png")
    titleImage = app.scaleImage(titleImage, 0.3)
    app.title = ImageTk.PhotoImage(titleImage)

    backgroundImage = app.loadImage("backgroundImage.jpg")
    backgroundImage = app.scaleImage(backgroundImage, 1.3)
    app.background = ImageTk.PhotoImage(backgroundImage)

    doorImage = app.loadImage("DoorClosed.png")
    doorImage = app.scaleImage(doorImage, 0.2)
    app.door = ImageTk.PhotoImage(doorImage)

    doorImage = app.loadImage("MetalgirlDoorOpen.png")
    doorImage = app.scaleImage(doorImage, 0.2)
    app.doorM = ImageTk.PhotoImage(doorImage)

    doorImage = app.loadImage("WoodboyDoorOpen.png")
    doorImage = app.scaleImage(doorImage, 0.2)
    app.doorW = ImageTk.PhotoImage(doorImage)

    woodboyImage = app.loadImage("Woodboy.png")
    woodboyImage = app.scaleImage(woodboyImage, 0.08)
    app.woodboy = ImageTk.PhotoImage(woodboyImage)

    metalgirlImage = app.loadImage("Metalgirl.png")
    metalgirlImage = app.scaleImage(metalgirlImage, 0.08)
    app.metalgirl = ImageTk.PhotoImage(metalgirlImage)

    switchLeftImage = app.loadImage("SwitchLeft.png")
    switchLeftImage = app.scaleImage(switchLeftImage, 0.08) #0.08 previously
    app.switchLeft = ImageTk.PhotoImage(switchLeftImage)

    switchRightImage = app.loadImage("SwitchRight.png")
    switchRightImage = app.scaleImage(switchRightImage, 0.08)
    app.switchRight = ImageTk.PhotoImage(switchRightImage)

    buttonImage = app.loadImage("Button.png")
    buttonImage = app.scaleImage(buttonImage, 0.1)
    app.button = ImageTk.PhotoImage(buttonImage)

    buttonPressedImage = app.loadImage("ButtonPressed.png")
    buttonPressedImage = app.scaleImage(buttonPressedImage, 0.06)
    app.buttonPressed = ImageTk.PhotoImage(buttonPressedImage)

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

    coinGImage = app.loadImage("coinG.png")
    coinGImage = app.scaleImage(coinGImage, 0.05)
    app.coinG = ImageTk.PhotoImage(coinGImage)

    coinBImage = app.loadImage("coinB.png")
    coinBImage = app.scaleImage(coinBImage, 0.05)
    app.coinB = ImageTk.PhotoImage(coinBImage)

    coinImage = app.loadImage("Coin.png")
    coinImage = app.scaleImage(coinImage, 0.05)
    app.coin = ImageTk.PhotoImage(coinImage)
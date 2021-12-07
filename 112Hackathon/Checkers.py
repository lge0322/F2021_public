
# imports
from cmu_112_graphics import *
from dataclasses import make_dataclass

######################################

def appStarted(app):
    # lists for Player's checkers
    app.P1checkers = []
    app.P2chckers = []
    # dataclass for Player checkers
    app.P1Checker = make_dataclass('P1Checker', ['row', 'col'])
    app.P2Checker = make_dataclass('P2Checker', ['row', 'col'])


# draw stuff!
def redraw_all(app, canvas):
    canvas.create_rectangle(0, 0, 40, 40, fill = 'red')

# run it!
def Checkers():
    runApp(width = 800, height = 800)

Checkers()
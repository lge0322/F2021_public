
from cmu_112_graphics import *

def reDrawAll(app, canvas):
    canvas.create_text(200, 100, text= "Amazing!")
    canvas.create_rectangle(100, 300, 800, 700, fill = 'turquoise',
                                outline = 'magenta',
                                        width = 10)
    
    canvas.create_oval(200, 100, 800, 700, fill = 'turquoise',
                                outline = 'magenta',
                                            width = 10)
# order matters a lot when creating graphics
runApp(width = 1000, height = 800)
#canvas - y increases downwards, so des x (rightwards)



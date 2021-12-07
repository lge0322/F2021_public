'''
things to do:

1. if characters collide with the wall, they die (probably not)
2. switches + buttons should work
3. the exit will be each others' doors
4. place gems 
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

from tkinter import *
from cmu_112_graphics import *


def appStarted(app):
    app.gameOver = False

    if woodboy.die or metalgirl.die:
        app.gameOver = True

    backgroundImage = app.loadImage("backgroundImage.jpg")
    app.backgroundImage = app.scaleImage(backgroundImage, 1.3)

    doorImage = app.loadImage("Door.jpeg")
    doorImage = app.scaleImage(doorImage, 0.4)
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
    switchRightImage = app.scaleImage(switchRightImage, 0.1)
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

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.switchOpen = False
        self.die = False

    
woodboy = Character(50, 50)  
metalgirl = Character(350, 350) 


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


class Cell:

    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""

        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'W': True, 'E': True}
        self.stack = []

    def all_walls(self):
        return all(self.walls.values())

    def remove_wall(self, other, wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

class Maze:

    def __init__(self, rows, cols, ix=0, iy=0):
        
        self.rows, self.cols = rows, cols
        self.ix, self.iy = ix, iy #initial position
        self.map = [[Cell(x, y) for y in range(cols)] for x in range(rows)] #giving the cell a location in the list
        self.north = self.south = self.east = self.west = 0
        self.wallListX = []
        self.wallListY = []
        self.wallPos = dict()
        self.w = 400 // rows
        self.switch = (0, 0)
        self.button = (0, 0)

    def getWallPos(self):
        for row in self.map:
            for col in row:
                x, y, dic = col.x, col.y, col.walls

                w = self.w

                r = self.w/2
                y = y * self.w 
                x = x * self.w 
                midX = x + r
                midY = y + r

                self.wallListX.append((x, x+w, y))
                self.wallListX.append((x, x+w, midY+r))
                self.wallListY.append((y, y+w, midX+r))
                self.wallListY.append((y, y+w, x))

                for val in dic:
                    if not dic[val]:
                        if val == "N":
                            self.wallListX.remove((x, x+w, y))
                        if val == "S":
                            self.wallListX.remove((x, x+w, midY+r))
                            
                        if val == "E":
                            self.wallListY.remove((y, y+w, midX+r))

                        if val == "W":
                            self.wallListY.remove((y, y+w, x))

    def canBeLift(self):
        res=  []
        for x in range(self.rows):
            for y in range(self.cols-3):
                i, j, k= self.map[x][y+1].walls["N"], self.map[x][y+2].walls["N"],self.map[x][y+3].walls["N"]
                if (not i and not j and not k) or (not i and not j and k): #the entire two rows should be empty
                    res.append((x,y))
        if len(res) == 0:
            return [(-5, -5)]

        return res
                
    def canBePlatform(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols):
                for key in self.map[x][y].walls:
                    if key == "S":
                        if self.map[x][y].walls[key]:
                            res.append((x, y))
        for val in res:
            if not self.canBeLift() == None:
                if val in self.canBeLift():
                    res.remove(val)
        
        if (0,0) in res:
            res.remove((0,0))
        if (self.rows-1, self.cols-1) in res:
            res.remove((self.rows-1, self.cols-1))

        return res

    def canBeHangingWood(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols):
                if self.map[x][y].walls["N"] and not self.map[x][y].walls["S"]:
                    res.append((x,y))
         #we don't need a cell that a wall in either north or south.
        
        for val in self.canBeLift():
            if val in res:
                res.remove(val)
        if (0, 0) in res: #delete a location of the character
            res.remove((0,0))
        return res

    def cellList(self, x, y):

        return self.map[x][y] 

    def validNext(self, cell):

        dxy = [('N', (0, -1)), ('S', (0, 1)), ('E', (1, 0)), ('W', (-1, 0))]

        nextList = []

        for direction, (dx, dy) in dxy:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.rows) and (0 <= y2 < self.cols):
                next = self.cellList(x2, y2)
                if next.all_walls():
                    nextList.append((direction, next))
        return nextList

    def __str__(self):

        maze_rows = ['-' * self.rows * 2]
        for y in range(self.ny):
            maze_row = ['|']
            for x in range(self.rows):
                if self.map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.rows):
                if self.map[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def isWallwithCharacter(self):
        for (x1, x2, y) in self.wallListX:
            if x1<= woodboy.x <= x2 and woodboy.y == y:
                    print('yes')
                    woodboy.die = True
            if x1<= metalgirl.x <= x2 and metalgirl.y == y:
                    metalgirl.die = True
                
        for (y1, y2, x) in self.wallListY:
            if y1 <= woodboy.y <= y2 and woodboy.x == x:
                print('yes')
                woodboy.die = True
            if y1 <= metalgirl.y <= y2 and metalgirl.x == x:
                metalgirl.die = True
            
    def draw(self, canvas):
        
        for row in self.map:
            for col in row:
                x, y, dic = col.x, col.y, col.walls
                
                w = self.w
                r = w/2
                y = y * w 
                x = x* w 
                midX = x + r
                midY = y + r
                self.north = canvas.create_line(x, y, x+w, y, fill= "black", width = 5)
                self.south = canvas.create_line(x, midY+r, x+w, midY+r, fill = "black", width = 5)
                self.east = canvas.create_line(midX+r, y, midX+r, y+w, fill = "black", width = 5)
                self.west = canvas.create_line(x, y, x, y+w, fill = "black", width =5)

                self.wallListX.append((x, x+w, y))
                self.wallListX.append((x, x+w, midY+r))
                self.wallListY.append((y, y+w, midX+r))
                self.wallListY.append((y, y+w, x))

                for val in dic:
                    if not dic[val]:
                        if val == "N":
                            canvas.delete(self.north)
                            self.wallListX.remove((x, x+w, y))

                        if val == "S":
                            canvas.delete(self.south)
                            self.wallListX.remove((x, x+w, midY+r))
                            
                        if val == "E":
                            canvas.delete(self.east)
                            self.wallListY.remove((y, y+w, midX+r))

                        if val == "W":
                            canvas.delete(self.west)
                            self.wallListY.remove((y, y+w, x))
    
    
                
    def drawDoor(self, app, canvas):
        canvas.create_image(50, 50, image = app.door)
        canvas.create_image(350, 350, image = app.door)
        
    def make_maze(self):

        n = self.rows * self.cols

        cell_stack = []

        currentCell = self.cellList(self.ix, self.iy)

        visited = 1 

        while visited < n: #until all the cells are visited 

            nextList = self.validNext(currentCell)
            
            if not nextList:
                currentCell = cell_stack.pop()
                continue
        
            direction, nextCell = random.choice(nextList) #this is a core of random map generation
            currentCell.remove_wall(nextCell, direction) #remove a wall
            cell_stack.append(currentCell) 
            currentCell = nextCell
            visited += 1



maze1 = Maze(4, 4, 0, 0)
maze2 = Maze(5, 5, 0, 0)
maze3 = Maze(6, 6, 0, 0)
maze4 = Maze(7, 7, 0, 0)
	
maze1.make_maze()
maze1.getWallPos()
maze1.isWallwithCharacter()


class Switch(Maze):
    def __init__(self, name):
        self.name = name
        self.x, self.y = random.choice(maze1.canBePlatform())
        maze1.switch = (self.x, self.y)
        self.isRight = False
        self.touched = False

    def draw(self, app, canvas):
        w = maze1.w
        r = w/2
        d = w/5
        x = self.x * w
        y = self.y * w

        if ((x <= metalgirl.x <= x+w and y<= metalgirl.y == y+w-r) or
                (x <= woodboy.x <= x+w and y<= woodboy.y == y+w-r)):
            self.isRight = True
            self.switchTouched = True
            canvas.create_image(x+r, y+w-d, image = app.switchRight)
        else:
            self.isRight = False
            canvas.create_image(x+r, y+w-d, image = app.switchLeft)


switch = Switch("switch")


class Lift(Maze):
    def __init__(self, name):
        self.name = name
        self.x, self.y = random.choice(maze1.canBeLift())
        self.speed = 5
        self.liftChar = False
        self.w = maze1.w
    
    def draw(self, app, canvas):
        w = self.w
        r = w/2
        d = w/5
        x = self.x * w
        y = self.y * w

        canvas.create_image(x+r, y+self.speed, image = app.lift)
    
    def move(self):
        for val in maze1.canBeLift():
            if val[0] == self.x and val[1] != self.y:
                maze1.canBeLift().remove(val)

        w = self.w
        curPos = self.y * w +self.speed
        if switch.isRight:
            self.speed += 5
            if curPos >= (self.y+2) * w:
                self.speed -= 5
            if woodboy.switchOpen:
                if metalgirl.x == self.x *w and metalgirl.y == curPos:
                    switch.isRight = False
                    self.liftChar = True
                    

        elif (not switch.isRight) and switch.touched:
                if woodboy.switchOpen:
                    if self.liftChar:

                        self.speed -= 5
                        metalgirl.speed -= 5

        else:
            while curPos <= (self.y *w):
                self.speed += 5
            

lift1 = Lift("lift1")
lift2=  Lift("lift2")


def removeAll():
    maze1.canBeLift().remove((lift1.x, lift1.y))
    maze1.canBePlatform().remove((switch.x, switch.y))
    

print('canbeplatform', maze1.canBePlatform())
print('canbelift', maze1.canBeLift())
print('canbehangingwood', maze1.canBeHangingWood())
 

removeAll()

class HangingWood(Maze):
    def __init__(self, name):
        self.name = name 
        self.x, self.y = random.choice(maze1.canBeHangingWood())
        self.w = maze1.w
        
    def draw(self, app, canvas):
        w = self.w
        r = self.w/2
        d = self.w/5
        canvas.create_image(self.x * w + r, self.y * w + r, image = app.hangingWood)

hangingwood1 = HangingWood("hangingwood1")

class Button(Maze):
    def __init__(self, name):
        self.name = name
        (x, y) = random.choice(maze1.canBePlatform())
        for val in maze1.canBePlatform():
            if (val[0] == x and val[1] != y) or (val[1] == y and val[0] != x):
                maze1.canBePlatform().remove(val)
        self.x, self.y = random.choice(maze1.canBePlatform())
        self.isPressed = False
        self.w = maze1.w

    def draw(self, app, canvas):
        w = self.w
        r = w/2
        d = w/5
        x = self.x * w
        y = self.y * w

        if ((x <= metalgirl.x <= x+w and y<= metalgirl.y == y+w-r) or
                (x <= woodboy.x <= x+w and y<= woodboy.y == y+w-r)):
            self.isPressed = True
            canvas.create_image(x+r, y+w-d, image = app.button)
        else:
            self.isPressed = False
            canvas.create_image(x+r, y+w-d, image = app.button)

button = Button("button")





class Obstacles:
    def __init__(self, x, y, name, type):

        self.x, self.y = x, y #random depending on the width, height of the platfrom (hardcoding)
        self.name = name
        self.speed = 0
        self.type = type

    def draw(self, app, canvas):
        w = 100
        if self.name == "lightning1":
            canvas.create_image(self.x, self.y + self.speed, image = app.lightning1)
        elif self.name == "lightning2":
            canvas.create_image(self.x, self.y + self.speed, image = app.lightning2)
        elif self.name == "lightning3":
            canvas.create_image(self.x, self.y + self.speed, image = app.lightning3)
        elif self.type == "waterdrop":
            canvas.create_image(self.x, self.y + self.speed, image = app.waterdrop)
    
    def move(self):
        self.speed = random.randint(3, 7)
        self.y += self.speed
        if self.y >= 400: #hardcode
            self.y = 0

    def isCharacterTouching(self):
        min = 10 #hardcode
        if self.type == "waterdrop":
            if (self.x - min <= woodboy.x <= self.x + min and 
                    self.y - min <= woodboy.y <= self.y + min ):
                    woodboy.die = True
        if self.type == "lightning":
            if (self.x - min <=metalgirl.x <= self.x + min 
                    and self.y - min <= metalgirl.y <= self.y + min):
                metalgirl.die = True
  
lightning1=  Obstacles(random.randint(0, 400), random.randint(0, 400), "lightning1", "lightning")
lightning2=  Obstacles(random.randint(0, 400), random.randint(0, 400), "lightning2", "lightning")
lightning3 = Obstacles(random.randint(0, 400), random.randint(0, 400), "lightning3", "lightning")
waterdrop1 = Obstacles(random.randint(0, 400), random.randint(0, 400), "waterdrop1", "waterdrop")
waterdrop2 = Obstacles(random.randint(0, 400), random.randint(0, 400), "waterdrop2",  "waterdrop")
waterdrop3 = Obstacles(random.randint(0, 400), random.randint(0, 400), "waterdrop3",  "waterdrop")


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

def redrawAll(app, canvas):
        canvas.create_image(200, 200, 
                            image = ImageTk.PhotoImage(app.backgroundImage)) #hardcode
        maze1.draw(canvas)
        maze1.drawDoor(app, canvas)
        
        canvas.create_image(woodboy.x, woodboy.y, image = app.woodboy)
        canvas.create_image(metalgirl.x, metalgirl.y, image = app.metalgirl)
        switch.draw(app, canvas)
        if not maze1.canBeLift() == None:
            lift1.draw(app, canvas)
            lift1.move()
            lift2.draw(app, canvas)
            lift2.move()
        hangingwood1.draw(app, canvas)
        button.draw(app, canvas)

        obstacleMove(app, canvas)
        
        if woodboy.die or metalgirl.die:
            canvas.create_text(200, 200, text = "Try again!")
            return

        
        
    
        
'''
    else:
        canvas.create_text(200, 200, text = "GAME OVER! TRY AGAIN", font = "Arial 12 bold")
    '''

runApp(width = 400, height = 400)

import random

################################################################################

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initX = x
        self.initY = y
        self.speed = 10
        self.die = False # check if characters touched the wall or obstacles

    
woodboy = Character(50, 50)  #fixed characters' position 
metalgirl = Character(350, 350) 

################################################################################
class Cell:

    wall_pairs = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'} #complements

    def __init__(self, x, y):

        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'W': True, 'E': True} #intialize all the directions to have walls
        self.stack = []

    def all_walls(self):
        return all(self.walls.values()) #see if a cell has all walls

    def collapse_wall(self, other, wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False #collapse the wall

################################################################################

class Maze:

    def __init__(self, rows, cols, ix=0, iy=0):
        
        self.rows, self.cols = rows, cols
        self.ix, self.iy = ix, iy #initial position
        self.map = [[Cell(x, y) for y in range(cols)] for x in range(rows)] #giving the cell a location in the list
        self.north = self.south = self.east = self.west = 0
        self.wallListX = []
        self.wallListY = []

        self.lift = True
        self.speed = 5
        
        self.gem = []
        self.coinList = []
        self.coinConsumed = []
        self.liftLoc = []

        self.res = []
        self.resB = []
        self.resG = []

        self.w = 400 // rows
        self.r = self.w // 2

        self.counter = 0

        self.numGem = 6 #hardcode

        self.isRight = False
        self.touched = False
        self.isPressed = False

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
            currentCell.collapse_wall(nextCell, direction) #append a wall
            cell_stack.append(currentCell) 
            currentCell = nextCell
            visited += 1

    def getWallPos(self):
        for row in self.map:
            for col in row:
                x, y, dic = col.x, col.y, col.walls

                w = self.w
                r = self.w/2
                y = y * w
                x = x * w
                midX = x + r
                midY = y + r

                for val in dic: #val = directions
                    if dic[val]: #when walls exist
                        if val == "N":
                            self.wallListX.append((x, x+w, y)) #north
                        elif val == "S":
                            self.wallListX.append((x, x+w, midY+r))
                        elif val == "E":
                            self.wallListY.append((y, y+w, midX+r))
                        elif val == "W":
                            self.wallListY.append((y, y+w, x))
                        

    #find locations for the lift ("N" of two or three columns should be False)
    def canBeLift(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols-3):
                
                #here, y is col, which is an actual x for tkinter. Same for x (row)
                
                i, j, k= self.map[x][y+1].walls["N"], self.map[x][y+2].walls["N"],self.map[x][y+3].walls["N"]
                
                if (not i and not j and not k) or (not i and not j and k): #the entire two rows should be empty
                    res.append((x,y+1)) 
        
        #if there are no such cells, just return None, as lifts are unnecessary for that stage
        if len(res) == 0:
            self.lift = False #checking if there's any possible location

        else:
            self.liftLoc = res

        return res
       
    '''
    Conditions for switches:
        1. the ground ("S") should be present
        2. they cannot be on the initial locations of the characters
        3. they cannot be on the same locations with lift
        4. they cannot be on the same locations with buttons
            - more specifically, not on the same row and not on the same col
        5. the number of the switches are equal to the number of the lifts 
        (as they operate the lifts)

    '''
    def canBeSwitch(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols):
                if ((x, y) == (0, 0) or (x, y) == (self.rows-1, self.cols-1) 
                        or (x, y) in self.canBeLift()): #2nd cond & 3rd cond
                    continue

                for key in self.map[x][y].walls:
                    if key == "S" and self.map[x][y].walls[key]: #1st cond
                            res.append((x, y))
        return res

    def canPlaceButton(self): #4th cond
        res = []
        for val in self.canBeSwitch():
            if not ((val[0] == self.x and val[1] == self.y) or 
                    (val[0] == self.x and val[1] != self.y)
                    or (val[0] != self.x and val[1] == self.y)):
                res.append(val)
        return res

    '''
    For hanging wood, if "N" and "S" of a cell are False (does not have a cell), 
    the condition is met.

    Exception: also avoid locations of the lift (since their conditions are somewhat similiar)
    '''
    def canBeHangingWood(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols-1):
                if ((x, y) == (0, 0) or (x, y) == (self.rows-1, self.cols-1)):
                    continue
                if self.lift and (x, y+1) in self.canBeLift(): #exception
                        continue
                if self.map[x][y].walls["N"] and not self.map[x][y].walls["S"]:
                    res.append((x,y))
        return res

#revisit##

    def canPlaceGem(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if (((x, y) == (0, 0) or 
                    (x, y) == (self.rows-1, self.cols-1))):
                    continue

                self.gem.append((x, y))
        

    def isWallwithCharacter(self):
        for (x1, x2, y) in self.wallListX:
            if x1<= woodboy.x + woodboy.speed <= x2 and woodboy.y + woodboy.speed == y:
                    woodboy.die = True
            if x1<= metalgirl.x + metalgirl.speed <= x2 and metalgirl.y + metalgirl.speed == y:
                    metalgirl.die = True
                
        for (y1, y2, x) in self.wallListY:
            if y1 <= woodboy.y <= y2 and woodboy.x == x:
                woodboy.die = True
            if y1 <= metalgirl.y <= y2 and metalgirl.x == x:
                metalgirl.die = True

    def consumed(self, app):
        d = self.r// 5
        for (x, y) in self.res:
            if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d) or 
                (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d)):
                self.counter += 1
                self.res.remove((x,y))

        for (x, y) in self.resG:
            if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d and self.isPressed) or 
                (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d and self.isPressed)):
                maze1.counter += 1
                self.resG.remove((x,y))

        for (x, y) in self.resB:
            if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d and self.isRight) or 
                (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d and self.isRight)):
                self.counter += 1
                self.resB.remove((x,y))

    def check(self, app):
        if self.counter == 2: #hardcode
            app.status = "Open"
            app.color = "green"
            app.doorOpen = True


#draw the maze!
    def allDraw(self, app, canvas):
        self.draw(self, canvas)
        self.drawDoor(app, canvas)
        self.drawButton(app, canvas)
        self.drawCoins(app, canvas)
        self.drawHangingWood(app, canvas)
        self.drawSwitch(app, canvas)
        self.drawInstructions(app, canvas)
        self.drawCoins(app, canvas)
        self.drawLift(app, canvas)
    
    def drawLift(self,app, canvas):

        for j in range(len(self.liftLoc)):
                w = app.w
                r = w/2
                x, y = self.liftLoc[j][0] * w + r, self.liftLoc[j][1] * w
                canvas.create_image(x, y+app.speed, image = app.lift)


    def draw(self, canvas):
        
        for row in self.map:
            for col in row:
                x, y, dic = col.x, col.y, col.walls
                
                w = self.w
                r = self.r
                y = y * w 
                x = x* w 
                midX = x + r
                midY = y + r
                self.north = canvas.create_line(x, y, x+w, y, fill= "black", width = 7)
                self.south = canvas.create_line(x, midY+r, x+w, midY+r, fill = "black", width = 7)
                self.east = canvas.create_line(midX+r, y, midX+r, y+w, fill = "black", width = 7)
                self.west = canvas.create_line(x, y, x, y+w, fill = "black", width = 7)

                self.wallListX.append((x, x+w, y))
                self.wallListX.append((x, x+w, midY+r))
                self.wallListY.append((y, y+w, midX+r))
                self.wallListY.append((y, y+w, x))

                for val in dic:
                    if not dic[val]:
                        if val == "N":
                            canvas.delete(self.north)
                            self.wallListX.append((x, x+w, y))

                        if val == "S":
                            canvas.delete(self.south)
                            self.wallListX.append((x, x+w, midY+r))
                            
                        if val == "E":
                            canvas.delete(self.east)
                            self.wallListY.append((y, y+w, midX+r))

                        if val == "W":
                            canvas.delete(self.west)
                            self.wallListY.append((y, y+w, x))

    def drawDoor(self, app, canvas): #fixed location
        if app.doorOpen:
            canvas.create_image(app.margin, app.margin, image = app.doorW)
            canvas.create_image(350, 350, image = app.doorM)
        
        else:
            canvas.create_image(50, 50, image = app.door)
            canvas.create_image(350, 350, image = app.door)
        
    def drawSwitch(self, app, canvas):
        (x, y) = random.choice(self.canBeSwitch())
        w= self.w
        r = self.r
        d = self.r // 5
        #check if 
        if ((x-r <= metalgirl.x <= x+r and y-r<= metalgirl.y == y+r) or
                (x-r <= woodboy.x <= x+r and y-r<= woodboy.y == y+r)):
            print('yesss')
            self.isRight = True
            self.isTouched = True
            canvas.create_image(x+r, y+w-d, image = app.switchRight)
        else:
            self.isRight = False
            canvas.create_image(x+r, y+w-d, image = app.switchLeft)

    def drawHangingWood(self, app, canvas):
        (x, y) = random.choice(self.canBeHangingWood())
        canvas.create_image(x * self.w + self.r, y * self.w + self.r, image = app.hangingWood)

    def drawButton(self, app, canvas):
        r = self.r
        w = self.r
        d = self.r // 5
        (x, y) = random.choice(self.canBeSwitch())

        canvas.create_image(x+r, y+w-d, image = app.self)
        
        if ((x <= metalgirl.x <= x+w and y<= metalgirl.y == y+w-r) or
                (x <= woodboy.x <= x+w and y<= woodboy.y == y+w-r)):
            self.isPressed = True

        else:
            self.isPressed = False

    def liftMove(self, app):
         for j in range(len(self.liftLoc)):
            w = app.w
            r = w/2
            x, y = self.liftLoc[j][0] * w + r, self.liftLoc[j][1] * w

            if self.isRight:
                if y <= self.liftLoc[j][1] + 2 * w:
                    app.speed += 5
    
            elif self.touched and not self.isRight:
                app.speed -= 5
            
            elif not self.touched and not self.isRight:
                pass
    
    def gemList(self):
        random.shuffle(self.gem)
        self.res = []
        sums = 0
        for i in range(2):
            w = self.w
            r = w/2
            d = r/2
            (x, y) = self.gem[i][0] * w + r, self.gem[i][1] * w +r
            sums+= 1
            self.res.append((x, y))

        self.resG = []
        for i in range(len(self.canPlaceButton())):
            (x, y) = self.gem[i][0] * w + r, self.gem[i][1] * w +r
            sums += 1
            self.resG.append((x, y))

        for i in range(len(self.canBeLift())):
            if len(self.canBeLift()) == 0:
                break
            (x, y) = self.gem[i][0] * w + r, self.gem[i][1] * w +r
            sums += 1
            self.resB.append((x, y))

    def drawCoins(self, app, canvas):
        for (x, y) in self.res: #revisit (increase the number of coins)
            coin = canvas.create_image(x, y, image = app.coin)
        if self.isRight:
            for (x, y) in self.resB:
                canvas.create_image(x, y, image = app.coinB)
        if self.isPressed:
                for (x, y) in self.resG:
                    canvas.create_image(x, y, image = app.coinG)
    

    def drawInstructions(self, app, canvas):
        if self.counter == self.numGem:
         canvas.create_text(470, 100, text = f'All coins are \n collected!', fill = "black", font = "Arial 12 bold")
        else:
            canvas.create_text(470, 100, text = f'Currently,\n {self.counter} coins \n are consumed', fill = "black", font = "Arial 12 bold")
    
    #indicating whether switches are open or not
        if self.isRight:
                canvas.create_text(470, 200, text = f'The self \n has been \n open!', fill = "black", font = "Arial 13 bold")
            
        elif self.touched and not self.isRight:
                canvas.create_text(470, 200, text = f'Currently, \n the self \n is not open', fill = "black", font = "Arial 13 bold")
        
################################################################################


#revisit#
maze1 = Maze(4, 4, 0, 0)
maze2 = Maze(5, 5, 0, 0)
maze3 = Maze(6, 6, 0, 0)
maze4 = Maze(7, 7, 0, 0)
	
maze1.make_maze()
maze1.getWallPos()
maze1.canPlaceGem()
maze1.gemList()
maze1.consumed()
maze2.make_maze()
maze2.getWallPos()

################################################################################

class Obstacles:
    def __init__(self, x, y, name, type):

        self.x, self.y = x, y #random depending on the width, height of the platfrom (hardcoding)
        self.name = name
        self.speed = 0
        self.type = type


    def draw(self, app, canvas):
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

################################################################################
lightning1=  Obstacles(random.randint(0, 400), random.randint(0, 400), "lightning1", "lightning")
lightning2=  Obstacles(random.randint(0, 400), random.randint(0, 400), "lightning2", "lightning")
lightning3 = Obstacles(random.randint(0, 400), random.randint(0, 400), "lightning3", "lightning")
waterdrop1 = Obstacles(random.randint(0, 400), random.randint(0, 400), "waterdrop1", "waterdrop")
waterdrop2 = Obstacles(random.randint(0, 400), random.randint(0, 400), "waterdrop2",  "waterdrop")
waterdrop3 = Obstacles(random.randint(0, 400), random.randint(0, 400), "waterdrop3",  "waterdrop")


################################################################################




################################################################################


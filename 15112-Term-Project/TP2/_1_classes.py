import random

################################################################################

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
#getWallpos
#canbelift, canbeswitch.... I think I can combine those together


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
        self.gemConsumed = []
        self.liftLoc = []

        self.w = 400 // rows
        self.counter = 0
        self.status = "closed"

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
    
    def mazeClear(self):
        if self.counter == 3: #hardcode
            self.status = "open"

    def canGoNext(self):
        if self.status == "open":
            #reset the app (but for the user it will look like going to the next level)
            pass

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
            if not ((val[0] == switch.x and val[1] == switch.y) or 
                    (val[0] == switch.x and val[1] != switch.y)
                    or (val[0] != switch.x and val[1] == switch.y)):
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
        res = []
        for x in range(self.rows):
            for y in range(self.cols):
                if (((x, y) == (0, 0) or 
                    (x, y) == (self.rows-1, self.cols-1))):
                    continue

                res.append((x, y))
        
        self.gem = res
   
        return res

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

#draw the maze!

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
        canvas.create_image(50, 50, image = app.door)
        canvas.create_image(350, 350, image = app.door)
        

################################################################################


#revisit#
maze1 = Maze(4, 4, 0, 0)
maze2 = Maze(5, 5, 0, 0)
maze3 = Maze(6, 6, 0, 0)
maze4 = Maze(7, 7, 0, 0)
	
maze1.make_maze()
maze1.getWallPos()

################################################################################

class Switch(Maze):
    def __init__(self, name):
        self.name = name
        self.x, self.y = random.choice(maze1.canBeSwitch())
        self.isRight = False
        self.touched = False

    def draw(self, app, canvas):
        w = maze1.w
        r = w/2
        d = w/5
        x = self.x * w
        y = self.y * w

        #check if 
        if ((x <= metalgirl.x <= x+r and y<= metalgirl.y == y+r) or
                (x <= woodboy.x <= x+r and y<= woodboy.y == y+r)):
            self.isRight = True
            canvas.create_image(x+r, y+w-d, image = app.switchRight)
        else:
            self.isRight = False
            canvas.create_image(x+r, y+w-d, image = app.switchLeft)


switch = Switch("switch")


################################################################################

################################################################################


################################################################################

class Gem:
    def __init__(self, name, x, y):
        self.name = name
        self.list = maze1.canPlaceGem()
        self.x, self.y = x, y
        self.w = maze1.w
        self.appear = 0 #created in order to delete coins
        self.delete = False


    def draw(self, app, canvas):
        if not self.delete:
            if self.name == "coinx":
                self.x, self.y = hangingwood1.x, hangingwood1.y
            r = self.w/2
            self.appear = canvas.create_image(self.x * self.w + r, self.y * self.w + r, image = app.coin)

    def isWithinRange(self):
        w= self.w
        x, y = self.x * w, self.y * w
        r = self.w/2

        
    
    def consume(self, canvas):
        if not self.delete:
            if self.isWithinRange():
                canvas.delete(self.appear)
                maze1.canPlaceGem().remove((self.x, self.y))
                self.delete = True



################################################################################
'''
coin1 = Gem("coin")
coin2 = Gem("coin")
coin3 = Gem("coin")
coin4 = Gem("coin")
coin5 = Gem("coin")
coinx = Gem("coinx") #this will be always above the hanging wood


print(coin1.x, coin1.y)
print(coin2.x, coin2.y)
print(coin3.x, coin3.y)
print(coin4.x, coin4.y)
print(coin5.x, coin5.y)
print(coinx.x, coinx.y)
'''
################################################################################



print('canbeswitch', maze1.canBeSwitch())
print('canbelift', maze1.canBeLift())
print('canbehangingwood', maze1.canBeHangingWood())
print('canplacegem', maze1.canPlaceGem())
print('canplacebutton', maze1.canPlaceButton())


################################################################################


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

################################################################################
hangingwood1 = HangingWood("hangingwood1")

################################################################################
class Button(Maze):
    def __init__(self, name):
        self.name = name
        self.x, self.y = random.choice(maze1.canPlaceButton())
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

################################################################################
button = Button("button")

################################################################################

class Obstacles:
    def __init__(self, x, y, name, type):

        self.x, self.y = x, y #random depending on the width, height of the platfrom (hardcoding)
        self.name = name
        self.speed = 0
        self.type = type
        self.w = maze1.w

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
    
    def drawBlock(self,app,canvas):
        self.x , self.y = lift1.x, lift1.y
        x, x2, y, y2 = self.x * self.w, self.x * self.w + self.w, self.y * self.w, (self.y+2) * self.w
        canvas.create_rectangle(x, x2, y, y2, fill = "black")

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
block1 = Obstacles(0, 0, "block", "block")

################################################################################




################################################################################


################################################################################
################################################################################
################################################################################


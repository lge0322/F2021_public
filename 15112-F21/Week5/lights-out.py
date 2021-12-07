#################################################
# lights-out.py
# Your Name: Gaeun (Ella) Lee
# Your AndrewID: gaeunl
# 
# Groupmate's Names: Alex Gillon
# Groupmate's AndrewIDs: agillon
#################################################

#################################################
# LightsOut!
# 
# Write the console-based game "LightsOut!"
# 
# Link to the writeup: https://docs.google.com/document/d/16ggNUsb0_Ddn6RMD2pStw0ZGkjAx8aTaoN4b0buTDII/edit?usp=sharing
# Link to the game: https://www.logicgamesonline.com/lightsout/
#################################################

#################################################
# Printing functions
#################################################

# Prints out the given 2D list input
def print2dList(a):
    if (a == []): print([]); return
    rows, cols = len(a), len(a[0])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(str(a[row][col])) for row in range(rows)])
    print('[')
    for row in range(rows):
        print(' [ ', end='')
        for col in range(cols):
            if (col > 0): print(', ', end='')
            print(str(a[row][col]).ljust(colWidths[col]), end='')
        print(' ]')
    print(']')

# Prints out the lightsOut solution for the hardcoded starting configuration 
# as a list of (row, col) tuples 
def printSolution():
    solution = [(0, 0), (0, 1), (0, 3), (0, 4), 
                (1, 2), (1, 3), (2, 1), (2, 3), 
                (2, 4), (3, 2), (3, 3), (4, 0), (4, 1)]

    print("Solution to the board:")
    for elem in solution:
        print(elem)

#################################################
# Gameplay
#################################################

# Initializes the starting configuration of the board
def makeStartingConfiguration():
    boardSize = 5
    board = [[0 for col in range(boardSize)] for row in range(boardSize)]
    board[0][2] = 1
    board[0][3] = 1
    board[1][0] = 1
    board[1][1] = 1
    board[1][4] = 1
    board[2][0] = 1
    board[2][1] = 1
    board[3][0] = 1
    board[3][1] = 1
    board[3][3] = 1
    board[4][3] = 1
    return board

#input function --> get (row, col) values --> when lists are all zeros,
#handling indexing errors (0,0) above and stuff
#work with numbers(if input != int, return False)
# This function is called to start the game of lightsOut!
def play():
    board = makeStartingConfiguration()
    print2dList(board)
    while not isTheGameOver(board):
        userTypeIn(board)
    return printSolution()
    

def userTypeIn(board):
    row = len(board)
    col = len(board[0])
    rowcolvalue = input('Enter the row and column value: ', )
    rowcolvalue = rowcolvalue.split(",")
    for i in range(len(rowcolvalue)):
        if not rowcolvalue[i].isdigit():
            return rowcolvalue
        if (int(rowcolvalue[i]) > row):
            return rowcolvalue
    return changeTheLight(rowcolvalue, board)

def changeTheLight(value, board):
    row = int(value[0])
    col = int(value[1])
    location = [        (-1, 0), #0
                (0, -1),        (0, 1),
                        (1, 0)         ] #3
    
    if board[row][col] == 1:
        board[row][col] = 0
    else:
        board[row][col] =1
    
    #consider four edge cases

    if ((row == 0) and (col == 0)): 
        for i in range(2, len(location)):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1
    
    elif (row, col) == (0, len(board)-1):
        for i in range(1, len(location), 2):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1
    
    elif (row, col) == (len(board)-1, 0):
        for i in range(0, len(location)-1, 2):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1
    
    elif ((row, col) == (len(board)-1, len(board)-1)):
        for i in range(len(location)-2):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1
    
    #consider positions on the bottom side 

    elif ((row == 0) and (col != 0) and (col != len(board)-1)):
        for i in range(1, len(location)):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1

    elif ((row == len(board)-1) and (col != 0) and (col != len(board)-1)):
        for i in range(len(location)-1):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1

    elif ((row != 0) and (row != len(board)-1) and (col == 0)):
        for i in (0, 2, 3):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1
    
    elif ((row != 0) and (row != len(board)-1) and (col == len(board)-1)):
        for i in (0, 1, 3):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1

    #consider the middle ones 

    else:
        for i in range(len(location)):
            crow = row+location[i][0] #continuing
            ccol = col+location[i][1]
            if board[crow][ccol] == 1:
                board[crow][ccol] = 0
            else:
                board[crow][ccol] = 1
    
    return board

def isTheGameOver(board):
    (rows, cols) = (len(board), len(board[0]))
    result = []
    for row in range(rows):
        for col in range(cols):
            result.append(board[row][col])
    if result.count(1) > 0: #1 should not be present
        return False
    return True

#################################################
# Top-level functions
#################################################

printSolution()   # uncomment me to print the solution to the starting board!
play()


#################################################
# hw10.py
#
# Your name: Gaeun Lee 
# Your andrew id: gaeunl
#################################################

import cs112_f21_week10_linter
import math, os

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def findLargestFile(path):
    # Wrapper to extract just the bestPath from the helper
    #initialize value to bestSize = 0, bestPath = ""
    return findLargestFileAndSize(path, 0, "")


def findLargestFileAndSize(path, bestSize, bestPath): 
    #some of the content is
    #from https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
    
    #check if the path is file
    if os.path.isfile(path): return path
    #if path is a folder then unzip it
    else:
        for filename in os.listdir(path):
            curFile = findLargestFileAndSize(path + "/" + filename, 
                                            bestSize, bestPath)
            #store the folder until there is no folder
            if not os.path.isfile(curFile): continue 
            curValue = os.path.getsize(curFile)
            if curValue >= bestSize:
                bestSize = curValue
                bestPath = curFile
    return bestPath

def knightsTour(rows, cols):
    board= make2dList(rows, cols)
    for row in range(rows):
        for col in range(cols):
            result = knightSolver(board, row, col, 1)
            if result != None:
                return result
    return None

def knightSolver(board, row, col, knightNumber):
    rows, cols = len(board), len(board[0])
    if knightNumber > rows * cols:
        return board
    else:
        moves= [(-2, -1), (-2, 1), (2, -1), (2, 1), 
                (-1, -2), (-1, 2), (1, -2), (1,2)]
        for (drow, dcol) in moves:
            newRow, newCol = row + drow, col + dcol
            if isLegalKnight(board, newRow, newCol):
                board[newRow][newCol] = knightNumber
                solution = knightSolver(board, newRow, newCol, knightNumber)
                if solution != None:
                    return solution
                board[newRow][newCol] = 0
        return None

def make2dList(rows, cols):
    return [([0]*cols) for row in range(rows)]

def isLegalKnight(board, newRow, newCol):
    rows, cols = len(board), len(board[0])
    if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
        return False

def knightsTour(rows, cols):
    board = [[-1]*cols for i in range(rows)] #create a board
    curRow, curCol, count = 0, 0, 1 #initialize values
    drow = [2, 1, -1, -2, -2, -1, 1, 2] #legal moves
    dcol = [1, 2, 2, 1, -1, -2, -2, -1]
    board[curRow][curCol] = 0
    #return the solution of the board otherwise None
    if knightsSolver(rows, cols, 
                        board, curRow, curCol, drow, dcol, count):
        return board
    else:
        return None
    

def isKnightLegal(row, col, board):
    if 0<=row<len(board) and 0<=col<len(board[0]) and board[row][col] == -1:
        return True 
    return False

def knightsSolver(rows, cols, board, curRow, curCol, drow, dcol, count):
    board[curRow][curCol] = count #store the count values to the board
    #base case
    if count == rows*cols:
        return True
    #recursive function
    else:
        numOfDirection = 8 #possible directions
        for num in range(numOfDirection):
            newRow = curRow + drow[num]
            newCol = curCol + dcol[num]
            if isKnightLegal(newRow, newCol, board):
                next = knightsSolver(rows, cols, board, newRow, newCol,
                                           drow, dcol, count+1)
                if next: return True
    board[curRow][curCol] = -1 
                #backtracking (pick up the wrongly placed knights)
    return False



#################################################
# Test Functions
#################################################

def testFindLargestFile():
    print('Testing findLargestFile()...', end='')
    assert(findLargestFile('sampleFiles/folderA') ==
                           'sampleFiles/folderA/folderC/giftwrap.txt')
    assert(findLargestFile('sampleFiles/folderB') ==
                           'sampleFiles/folderB/folderH/driving.txt')
    assert(findLargestFile('sampleFiles/folderB/folderF') == '')
    print('Passed!')

def testKnightsTour():
    print('Testing knightsTour()....', end='')
    def checkDims(rows, cols, ok=True):
        T = knightsTour(rows, cols)
        s = f'knightsTour({rows},{cols})'
        if (not ok):
            if (T is not None):
                raise Exception(f'{s} should return None')
            return True
        if (T is None):
            raise Exception(f'{s} must return a {rows}x{cols}' +
                             ' 2d list (not None)')
        if ((rows != len(T)) or (cols != (len(T[0])))):
            raise Exception(f'{s} must return a {rows}x{cols} 2d list')
        d = dict()
        for r in range(rows):
            for c in range(cols):
                d[ T[r][c] ] = (r,c)
        if (sorted(d.keys()) != list(range(1, rows*cols+1))):
            raise Exception(f'{s} should contain numbers' +
                             ' from 1 to {rows*cols}')
        prevRow, prevCol = d[1]
        for step in range(2, rows*cols+1):
            row,col = d[step]
            distance = abs(prevRow - row) + abs(prevCol - col)
            if (distance != 3):
                raise Exception(f'{s}: from {step-1} to {step}' +
                                 ' is not a legal move')
            prevRow, prevCol = row,col
        return True
    assert(checkDims(4, 3))
    assert(checkDims(4, 4, ok=False))
    assert(checkDims(4, 5))
    assert(checkDims(3, 4))
    assert(checkDims(3, 6, ok=False))
    assert(checkDims(3, 7))
    assert(checkDims(5, 5))
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testFindLargestFile()
    testKnightsTour()

def main():
    cs112_f21_week10_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
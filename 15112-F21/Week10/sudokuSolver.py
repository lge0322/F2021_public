#----------------
# Functions that we assume are written and correct:
#----------------

#returns list of possible legal values for the given row col
def findPossibleValues(board, row, col):
    return []

#returns an empty spot on the board as tuple i.e. (row, col)
def findNextEmptyEntry(board):
    return (42,42) 

#returns true if the board is legal, false otherwise, by checking all of the sudoku rules
def isLegalBoard(board):
    return 42

def countValue(board, value):
    counter = 0
    rows = len(board)
    for row in range(rows):
        cols = len(board[row])
        for col in range(cols):
            curVal = board[row][col]
            if curVal == value:
                counter += 1
    return counter
    
# DO NOT CHANGE THE FUNCTIONS ABOVE, ASSUME THAT THEY ARE CORRECT AND JUST
# WORK ON THE solveSudoku PROBLEM


def solveSudoku(board):
    if countValue(board, 0) == 0: #helper function that counts zero in a board
        if isLegalBoard(board):
            return board
        else:
            return None
    else:
        nextRow, nextcol = findNextEmptyEntry(board)
        possibleValues = findPossibleValues(board, nextRow, nextCol)
        for possiblevalue in possibleValues:
            board[newRow][newcol] = possibleValue
            solution = solveSudoku(board)
            if solution != None:
                return board
        board[newRow][newCol] = 0
        return None
            
        


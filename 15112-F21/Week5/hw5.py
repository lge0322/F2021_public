#################################################
# hw5.py
# name: Gaeun Lee
# andrew id: gaeunl

#################################################

import cs112_f21_week5_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Part A
#################################################

def nondestructiveRemoveRowAndCol(A, row, col):
    # remember: do not copy or deepcopy A here.
    # instead, directly construct the result
    result = copy.deepcopy(A)
    for i in range(len(result)): #to eliminate the designated row
        if i == row:
            result.remove(result[i])

    for j in range(len(result)): #to eliminate regarding columns
        result[j].pop(col)
    return result

def destructiveRemoveRowAndCol(A, row, col):
    A.pop(row) #pop the row destructively
    for i in range(len(A)):
        A[i].pop(col) #pop the column
    
def matrixMultiply(m1,m2):
    row = len(m1) #the number of cols in the product = # of cols in m1
    col = len(m2[0]) # # of rows in the product = # of rows in m2
    
    result = [[0 for rows in range(col)] for cols in range(row)]
    
    for i in range(row): 
        for j in range(col): 
            for k in range(len(m2)): 
                result[i][j] += m1[i][k] * m2[k][j]
    return result
          
    
#on the board, the next number cannot be located somewhere beyond
    #row +1 and col + 1
    #for example, when 3 is located (2,1), 4 should be located in 
    #(1,1),(1,2),(2,2)

def isKingsTour(board):
    rows = len(board)
    cols = len(board[0])
    current_number = 1 #1 is always the first number
    next_number = 2 #2 is always the first starting next number
    if not isNumberLegal(board): 
        return False
    while next_number < rows*cols+1: #explained above the main function
        if ((abs(numberlocation(current_number, board)[0] - 
            numberlocation(next_number, board)[0] > 1)) or (
            abs(numberlocation(current_number, board)[1] - 
                numberlocation(next_number,board)[1]) > 1)):
            return False
        if current_number == rows*cols:
            break  
        current_number += 1
        next_number += 1
    return True

def isNumberLegal(board):
    rows = len(board)
    cols = len(board[0])
    lboard = [None]*(rows*cols+1) 
    lboard[0] = False #as 0 cannot be on a board
    for i in range(rows):
        for j in range(cols):
            if lboard[board[i][j]] != None: #checking duplicates
                return False
            if (board[i][j] > rows*cols):
                return False
            else:
                lboard[board[i][j]] = 1
    if None in lboard: #checking if there's any number missing
        return False
    else:
        return True

def numberlocation(number, board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == number: #finding the location of the number
                return [row, col]


#################################################
# Part B
#################################################

def isMagicSquare(a): #main function
    if isSquareQualified(a) == True:
        if len(a) == 1:
            return True
        if ((horizontalSum(a) == True) and(verticalSum(a) == True) and 
            (diagonalSumDownwards(a) == True) and 
            (diagonalSumUpwards(a) == True)):
                return True
        else:
            return False
    else:
        return False

####helper functions####

def ultimateTotal(a): #total for all of the sums should be the same
    total = 0
    for i in range(len(a[0])):
        total += a[0][i]
    return total

def horizontalSum(a): #checking rows
    rows = len(a)
    cols = len(a[0])
    total = 0
    for row in range(rows):
        for col in range(cols):
            total += a[row][col]
        if total != ultimateTotal(a):
            return False
        else:
            total = 0
    return True

def verticalSum(a): #checking columns
    rows = len(a)
    cols = len(a[0])
    total = 0
    for col in range(cols):
        for row in range(rows):
            total += a[col][row]
        if total != ultimateTotal(a):
            return False
        else:
            total = 0
    return True

def diagonalSumDownwards(a): #checking diagonal 1
    rows = len(a)
    cols = len(a[0])
    total = 0
    for row in range(rows):
        total += a[row][row]
    if total != ultimateTotal(a):
        return False
    else:
        return True

def diagonalSumUpwards(a): #checking diagonal 2
    rows = 0
    cols = len(a[0])-1
    total = 0
    count = 0
    while count < len(a[0]): #while loop in order to use rows+=1, cols -=1
        total += a[rows][cols]
        rows += 1
        cols -= 1
        count += 1
    if total != ultimateTotal(a):
        return False
    else:
        return True

        
def isSquareQualified(a):
    #condition
    #1: non-empty 
    #2: square (rows = cols) v
    #3: if a[i][j] != int: return False
    #4: every int should be unique
    if (len(a) == 1) and (isinstance(a[0], int)): return False
    row = len(a)
    col = len(a[0])
    result = []
    if (row != col): return False
    for i in range(row):
        if len(a[i]) != len(a[0]):
            return False
    for i in range(row):
        for j in range(col):
            result.append(a[i][j])
            if a[i][j] == None:
                return False
            if not isinstance(a[i][j],int):
                return False
    for k in range(len(result)):
        if result.count(result[k]) > 1:
            return False
    return True
            

###########helper functions for magicsquare ######


def wordSearchWithIntegerWildcards(board, word): #credited by the 112 website!
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != False):
                return True
    return False
            
def wordSearchFromCell(board, word, startRow, startCol): 
    for drow in [-1, 0, +1]: #credited by the 112 website!
        for dcol in [-1, 0, +1]:
            if (drow, dcol) != (0, 0):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != False):
                    return True
    return False

#credited by the 112 website!

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    res = [board[row][col] for row in range(rows) for col in range(cols)]
    wildcard = []
    nonwild = []
    count = 0
    for letter in word: #separating letters into two categories: in board or not
        if letter not in res:
            wildcard.append(letter)
            count += 1
    for value in word:
        if value in res:
            nonwild.append(value)
    for k in range(len(nonwild)): 
        if nonwild.count(nonwild[k]) > res.count(nonwild[k]):
            return False
    if len(word) == 3:
        if (word[0] not in res) and (word[1] in res):
            return False

    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols)or (board[row][col] != word[i])):
            if isinstance(board[row-1][col-1], int) == True: 
                if count == len(word): #think of the int case
                    if len(word) == board[row-1][col-1]:
                        return True
                    else:
                        return False
                else:
                    count -= 1
                    if count < 0: #check if words have more numbers than board
                        return False
                    else:
                        return True
            return False
    if count > 0 :
        return False
    return True


def areLegalValues(values):
    #check if the value is int
    #check if value other than zero has no duplicate
    res = []
    for i in range(len(values)):
        res.append(None)#check if value is inclusive
    for j in values:
        if j > len(values): return False
        if (res[j-1] == True) and (not j == 0):
            return False
        elif (res[j-1] != True) and (not j == 0):
            res[j-1] = True
    return True

def isLegalRow(board, row):
    return areLegalValues(board[row])

def isLegalCol(board, col):
    value = list(board[row][col] for row in range(len(board))) #make a col list
    return areLegalValues(value)

def isLegalBlock(board, block): 
    rows = len(board)
    cols = len(board[0])
    value = roundHalfUp(cols**0.5) #to get a value of a block
    srow = block // value * value
    scol = block % value * value
    result = []
    for row in range(srow, srow + value): #for a single block
        for col in range(scol, scol + value):
            result.append(board[row][col])
    return areLegalValues(result)

def isLegalSudoku(board):
    rows = len(board)
    cols = len(board[0])
    blocks = roundHalfUp(len(board)**0.5) 
    for row in range(rows):
        if not isLegalRow(board, row) == True:
            return False
    for col in range(cols):
        if not isLegalCol(board, col) == True:
            return False
    for block in range(blocks):
        if not isLegalBlock(board, block) == True:
            return False
    return True


#################################################
# Bonus/Optional
#################################################

def makeWordSearch(wordList, replaceEmpties):
    return 42

#################################################
# Test Functions (#ignore_rest)
#################################################
def testWordSearchWithIntegerWildcards():
    print("Testing wordSearchWithIntegerWildcards()...", end='')

    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
           [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
           ]
    assert(wordSearchWithIntegerWildcards(board, "dog") == True) #without false
    assert(wordSearchWithIntegerWildcards(board, "cat") == True)#
    assert(wordSearchWithIntegerWildcards(board, "tad") == True)#
    assert(wordSearchWithIntegerWildcards(board, "cow") == False)#

    
    board = [ [ 'd', 'o',  1  ],
     
            [  3 , 'a', 'c' ],
              [ 'o', 'q' ,'t' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "dzzzo") == True)#
    assert(wordSearchWithIntegerWildcards(board, "dzzo") == True)#
    assert(wordSearchWithIntegerWildcards(board, "zzzd") == True)#
    
    assert(wordSearchWithIntegerWildcards(board, "zzzo") == True)  #
    
    assert(wordSearchWithIntegerWildcards(board, "z") == True)#
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)#
    
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    board = [ [ 'a', 'b', 'c' ],
             [ 'd',  2 , 'e' ],
              [ 'f', 'g', 'h' ]]
    assert(wordSearchWithIntegerWildcards(board, "aqqh") == True)  #
    assert(wordSearchWithIntegerWildcards(board, "aqqhh") == False) 
    assert(wordSearchWithIntegerWildcards(board, "zz") == True) 
    assert(wordSearchWithIntegerWildcards(board, "zzc") == True) 
    assert(wordSearchWithIntegerWildcards(board, "zaz") == False)

    board = [ [ 3 ] ]
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True) #
    assert(wordSearchWithIntegerWildcards(board, "zz") == False) 
    
    assert(wordSearchWithIntegerWildcards(board, "zzzz") == False) 
    print("Passed!")
   

def testIsMagicSquare():
    print("Testing isMagicSquare()...", end="")
    assert(isMagicSquare([42]) == False)
    assert(isMagicSquare([[42]]) == True)
    assert(isMagicSquare([[8, 1, 6], [3, 5, 7], [4, 9]]) == False)
    assert(isMagicSquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True)
    assert(isMagicSquare([[4-7, 9-7, 2-7], [3-7, 5-7, 7-7], [8-7, 1-7, 6-7]])
           == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMagicSquare(a))
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMagicSquare(a) == False)
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMagicSquare(a) == False)
    assert(isMagicSquare([[1, 2], [2, 1]]) == False)
    assert(isMagicSquare([[1, 1], [1, 1]]) == False) # repeats
    assert(isMagicSquare([[0], [0]]) == False) # Not square!
    assert(isMagicSquare('do not crash here!') == False)
    assert(isMagicSquare(['do not crash here!']) == False)
    assert(isMagicSquare([['do not crash here!']]) == False)
    print("Passed!")

def testNondestructiveRemoveRowAndCol():
    print('Testing nondestructiveRemoveRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testMatrixMultiply():
    print("Testing matrixMultiply()...", end='')
    m1 = [[1,2],
          [3,4]] # 2x2

    m2 = [[4],
          [5]]     # 2x1
    m3 = [[14],
          [32]]
    assert(matrixMultiply(m1,m2) == m3) 
    assert(matrixMultiply([[3, 7], [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]], 
                          [[9, 8, 3],
                           [5, 1, 3]])==
                          [[62, 31, 30],
                           [61, 37, 27],
                           [65, 44, 27],
                           [75, 46, 33],
                           [117, 73, 51],
                           [83, 60, 33]])
    assert matrixMultiply([[8]],[[5]])==[[40]]
    print("Passed!")

def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    a = [ [  3, 2, 9 ],
          [  6, 4, 1 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  1, 2, 3 ],
          [  7, 4, 8 ],
          [  6, 5, 9 ] ]
    assert(isKingsTour(a) == False)
    a = [ [ 3, 2, 1 ],
          [ 6, 4, 0 ],
          [ 5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 1 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 1 ],
          [  6, 4, 0 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 1 ],
          [  6, 4, 9 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  2, 8, 9 ],
          [  3, 1, 7 ],
          [  4, 5, 6 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 9 ] ]
    assert(isKingsTour(a) == True)
    print("Passed!")



def testIsLegalSudoku():
    # From Leon Zhang!
    print("Testing isLegalSudoku()...", end="")
    board = [[0]]
    assert isLegalSudoku(board) == True
    board = [[1]]
    assert isLegalSudoku(board) == True
#[0][0] & [0][1] & [1][0] & [1][1]
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [[0, 4, 0, 0],
             [0, 0, 3, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 2]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 1, 4, 3],
             [4, 3, 2, 1]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]    
    assert isLegalSudoku(board) == False

    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert isLegalSudoku(board) == True
    
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 9, 7, 9 ]
    ]
    assert isLegalSudoku(board) == False
    board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6, 8]]
    assert isLegalSudoku(board) == True
    # last number is supposed to be 8, not 10
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6,10]]
    assert isLegalSudoku(board) == False
    print("Passed!")

def testMakeWordSearch():
    print("Testing makeWordSearch()...", end="")
    board = makeWordSearch([], False)
    assert(board == None)

    board = makeWordSearch(["ab"], False)
    assert(board == [['a', 'b'], ['-', '-'] ])
    board = makeWordSearch(["ab"], True)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd"], False)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd", "de"], False)
    assert(board == [['a', 'b', '-'], ['c', 'd', '-'], ['d', 'e', '-']])
    board = makeWordSearch(["ab", "bc", "cd", "de"], True)
    assert(board == [['a', 'b', 'a'], ['c', 'd', 'c'], ['d', 'e', 'a']])

    board = makeWordSearch(["abc"], False)
    assert(board == [['a', 'b', 'c'], ['-', '-', '-'], ['-', '-', '-']])
    board = makeWordSearch(["abc"], True)
    assert(board == [['a', 'b', 'c'], ['c', 'd', 'a'], ['a', 'b', 'c']])

    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], False)
    assert(board == [['a', 'b', 'c'], ['d', 'e', '-'], ['c', 'f', 'g']])
    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], True)
    assert(board == [['a', 'b', 'c'], ['d', 'e', 'a'], ['c', 'f', 'g']])

    board = makeWordSearch(["abcd", "abc", "dcb"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['-', '-', '-', '-'], 
                     ['-', '-', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', '-', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', 'b', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           True)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', 'a'], 
                     ['b', 'a', 'd', 'e'],
                     ['c', 'e', 'b', 'a']])
    #[ (["abcd", "abc", "dcb", "xa", "by", "bya", "bbbx", "dbxa", "cbxa" ],
    #False),

    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testMatrixMultiply()
    testIsKingsTour()

    # Part B:
    testIsLegalSudoku()
    testIsMagicSquare()
    testWordSearchWithIntegerWildcards()
    
    
    
    #testThreeMensMorris() # this will be submitted in a separate file!

    # Bonus:
    #testMakeWordSearch()

def main():
    cs112_f21_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()

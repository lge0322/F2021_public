def isIncreasingBishopsTour(board):
    return helper(board, 0, 0)
            
        
                

def isLegal(board, row, col):
    if 0<=row<len(board) and 0<=col<len(board[0]):
        return True
    else:
        return False

def isIncreasing(board, curRow, curCol):
    rows, cols = len(board), len(board[0])
    if row == 0 and col == cols-1:
        return True
    else:
        for (dx, dy) in [(-1, -1), (1, -1), (-1, 1), (1,1)]:
            for magnitude in range(rows):
                tempRow, tempCol = (row + dx*magnitude, col + dy*magnitude)
                if (0 <=tempRow and tempRow < rows and 0 <= tempCol and tempCol < cols and:
                    board[row][col] < board[tempRow][tempCol]):
                    solution = isIncreasing(board, tempRow, tempCol)
                    if solution != False:
                        return True
            return False

def testIsIncreasingBishopsTour():
    print("Testing isIncreasingBishopsTour", end="...")
    board1 = [  [0, 0, 7],
                [5, 3, 8],
                [9, 7, 6]   ]
    assert(isIncreasingBishopsTour(board1) == True)
    board2 = [  [0, 0, 7, 8],
                [5, 3, 8, 2],
                [9, 7, 6, 4],
                [1, 3, 9, 2]  ]
    assert(isIncreasingBishopsTour(board2) == False)
    print("Passed")

testIsIncreasingBishopsTour()

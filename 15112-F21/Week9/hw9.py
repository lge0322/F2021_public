#################################################
# hw9.py

# Your name: Gaeun Lee
# Your andrew id: gaeunl
#################################################

import cs112_f21_week9_linter
import math, copy, os

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

def oddCount(L):
    if len(L) == 0: return 0
    else:
        return (L[0]%2) + oddCount(L[1:]) #as odd % 2 = 1

'''
solution

    if len(L) == 0: return 0
    elif L[0] % 2 == 0: return oddCount(L[1:])
    else: return 1 + return oddCount(L[1:])
'''

def oddSum(L):
    if len(L) == 0: return 0 #base case returns 0
    else:
        if L[0] % 2 == 1:
            return (L[0]) + oddSum(L[1:]) #sums up all the values
    return oddSum(L[1:])

'''
solution

    if L== []: return 0
    elif L[0] % 2 == 1:
        return L[0] + oddSum(L[1:])
    else:
        oddSum(L[1:])

'''

def oddsOnly(L):
    if len(L) == 0: return L #base case returns the empty list
    if L[0] % 2 == 1:
        return [L[0]] + oddsOnly(L[1:]) #adds only odds
    return oddsOnly(L[1:])

'''
solution

    if L == []:
        return []
    elif L[0] % 2 ==1:
        return [L[0]]+ oddsOnly(L[1:])
    else:
        return oddsOnly(L[1:])

'''
def maxOdd(L):
    if len(L) == 0: return None
    else:
        nextOdd = maxOdd(L[1:]) #set the variable for recursion
        if L[0] % 2 == 1:
            if nextOdd == None:
                return L[0]
            return isBigger(L[0], nextOdd) #compare a value with rest
    return nextOdd

'''
solution

    if L== []: return None
    else:
        first= L[0]
        rest = maxOdd(L[1:])
        if first % 2 == 1 and rest == None or first > rest:
            return first
        else:
            return rest
        
'''
def isBigger(n, L): #comparing values
    if n > L: return n 
    else: return L



def hasConsecutiveDigits(n):
    return isConsecutive(abs(n), abs(n)//10) #use a wrapper function

def isConsecutive(n, value):
    if n == 0: return False #base case
    else:
        curVal = n % 10 #the last digit
        nextVal = value % 10 #second to last digit
        if curVal == nextVal: 
            return True
        else:
            return isConsecutive(n//10, value//10) 

'''
solution

    n = abs(n)
    if n == 0: return False
    elif n % 10 == (n // 10) % 10:
        return True
    else:
        return hasConsecutiveDigits(n//10)
'''
def alternatingSum(L):
    return alternatingSumHelper(L, 0)

def alternatingSumHelper(L, sum):
    check = True #represents even terms; False represents odd terms
    if len(L) == 0: #base case
        return 0
    else:
        if check == True: 
            check = False #change the boolean value for the next value in L
            return L[0] - alternatingSumHelper(L[1:], sum)
        else:
            check = True
            return L[0] + alternatingSumHelper(L[1:], sum)

'''
solution

    if L == []: return 0
    elif len(L) % 2 == 0:
        return alternatingSum(L[:-1]) - L[-1]
    else:
        return alternatingSum(L[:-1]) + L[-1]
'''
#################################################
# Freddy Fractal Viewer
#################################################

from cmu_112_graphics import *

import tkinter as tk 

def appStarted(app):
    app.level = 0

def drawFractal(app, canvas, level, x, y, size): 
    #bear face
    canvas.create_oval(x-size,y-size,x+size, y+size, fill= 'brown', 
                        outline = 'black', width = size//12)
    #bear lip area
    x1, y1 = size//2, size//3.5
    canvas.create_oval(x-x1, y-y1*0.8, x+x1, 
                            y+y1*2.8, width=size//15, fill ='navajo white3')
    #bear nose
    x2, y2 = size//7.5, size//5.5
    canvas.create_oval(x-x2*1.2, y-y2*0.6, x+x2*1.2, y+y2*1.2, fill = 'black')

    #bear eyes
    canvas.create_oval(x-x2*4.3, y-y2-size**0.83, x-x2*1.9,y+y2-size**0.83, 
                            fill = 'black')
    canvas.create_oval(x+x2*1.8, y-y2-size**0.83, x+x2*4.2,y+y2-size**0.83, 
                            fill = 'black')
    #lips
    newLipsR = size // 9
    canvas.create_arc(x-newLipsR*2.8, y+newLipsR*3, 
                            x-newLipsR*0.2, y+newLipsR*5.2, 
                            start=180, extent=180, style=tk.ARC, width=size//20)
    canvas.create_arc(x-newLipsR*0.1, y+newLipsR*3, 
                            x+newLipsR*2.5, y+newLipsR*5.2, 
                            start=180, extent=180, style=tk.ARC, width=size//20)

    if level == 0: pass #base case
    else: #recursion
        drawFractal(app, canvas, level-1, x+size*1.05, y-size*1.05, size/2)
        drawFractal(app, canvas, level-1, x-size*1.05, y-size*1.05, size/2)

def keyPressed(app, event): #from 15112 notes
    if event.key in ['Up', 'Right']:
        app.level += 1
        if app.level > 5: 
            app.level -= 1
    elif (event.key in ['Down', 'Left']) and (app.level > 0):
        app.level -= 1

def redrawAll(app, canvas): #from 15112 notes
    margin = min(app.width, app.height)//10
    x, y, size= app.width//2, app.height//1.5, app.width//4 #set initial values
    drawFractal(app, canvas, app.level, x, y, size)
    canvas.create_text(app.width/2, 0,
                       text = f'Level {app.level} Fractal',
                       font = 'Arial ' + str(int(margin/3)) + ' bold',
                       anchor='n')
    canvas.create_text(app.width/2, margin,
                       text = 'Use arrows to change level',
                       font = 'Arial ' + str(int(margin/4)),
                       anchor='s')

def runFreddyFractalViewer():
    print('Running Freddy Fractal Viewer!')
    runApp(width=400, height=400)

'''
solution

    def drawFractal(app, canvas, level, x, y, r):
         m = r//10
         if level ==0 :
             teddyFace(app.canvas, x, y, r)
            else:
                drawFractal(app, canvas, level-1, x-r, y-r, r/2)
                drawFractal(app, canvas, level-1, x+r, y-r, r/2)
                teddyFace(app.canvas, x, y, r)
    
    def keyPressed(app, event):
        if event.key in ['Up', 'Right']:
            app.level += 1
        elif event.key in ['Down', 'Left'] and app.level >0:
            app.level -= 1
            
    def teddyFace(app, canvas, xc, yc, r):
        w = r//10
        canvas.create_oval(xc-r, yc-r, xc+r, yc+r, width = w, 
                            fill = 'firebrick')
        snoutYC, snouthR = yc + r//3, r//2
        canvas.create_oval(xc-snoutR, snouthYC, snoutR, xc+snoutR, snouthYC +
                                snoutR, width = snoutR//10, fill = 'tan')
        dotR = r//6
        noseYC = yc + r//5
        canvas.create_oval(xc-dotR, noseYC-dotR, xc+dotR, noseYC + dotR, fill = 'black')
        mouthYC, mouthYR, mouthXR = snoutYC+snoutR//3, snoutR//4, snoutR//2
        canvas.create_arc(xc-mouthXR, mouthYC - mouthYR, xc, mouthYC+mouthYR, outline = 'black', 
                            style="arc", extent = -180, width = snouthR//10)
        canvas.create_arc(xc, mouthYC - mouthYR, xc+mouthXR, mouthYC+mouthYR, outline = 'black', 
                            style="arc", extent = -180, width = snouthR//10)
        leftEyeXC, rightEyeXC, eyeYC = xc-r/3, xc+r/3,yc-r//2
        canvas.create_oval(leftEyeXC-dotR, eyeYC-dotR, leftEyeXC+dotR, rightEyeXC+dotR, fill = 'black')
        canvas.create_oval(rightEyeXC-dotR, eyeYC-dotR, rightEyeXC+dotR, rightEyeXC+dotR, fill = 'black')

        In RedrawAll(app, canvas):
        drawFractal(app, canvas, app.level, app.width/2, app.height/1.5, app.width/4)
'''
#################################################
# Test Functions
#################################################

def testOddCount():
    print('Testing oddCount()...', end='')
    assert(oddCount([ ]) == 0)
    assert(oddCount([ 2, 4, 6 ]) == 0) 
    assert(oddCount([ 2, 4, 6, 7 ]) == 1)
    assert(oddCount([ -1, -2, -3 ]) == 2)
    assert(oddCount([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 6)
    print('Passed!')

def testOddSum():
    print('Testing oddSum()...', end='')
    assert(oddSum([ ]) == 0)
    assert(oddSum([ 2, 4, 6 ]) == 0) 
    assert(oddSum([ 2, 4, 6, 7 ]) == 7)
    assert(oddSum([ -1, -2, -3 ]) == -4)
    assert(oddSum([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 1+3+5+7+9+11)
    print('Passed!')

def testOddsOnly():
    print('Testing oddsOnly()...', end='')
    assert(oddsOnly([ ]) == [ ])
    assert(oddsOnly([ 2, 4, 6 ]) == [ ]) 
    assert(oddsOnly([ 2, 4, 6, 7 ]) == [ 7 ])
    assert(oddsOnly([ -1, -2, -3 ]) == [-1, -3])
    assert(oddsOnly([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == [1,3,5,7,9,11])
    print('Passed!')

def testMaxOdd():
    print('Testing maxOdd()...', end='')
    assert(maxOdd([ ]) == None)
    assert(maxOdd([ 2, 4, 6 ]) == None) 
    assert(maxOdd([ 2, 4, 6, 7 ]) == 7)
    assert(maxOdd([ -1, -2, -3 ]) == -1)
    assert(maxOdd([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 11)
    print('Passed!')

def testHasConsecutiveDigits():
  print('Testing hasConsecutiveDigits()...', end='')
  assert(hasConsecutiveDigits(1123) == True)
  assert(hasConsecutiveDigits(-1123) == True)
  assert(hasConsecutiveDigits(1234) == False)
  assert(hasConsecutiveDigits(0) == False)
  assert(hasConsecutiveDigits(1233) == True)
  print("Passed!")

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testOddCount()
    testOddSum()
    testOddsOnly()
    testMaxOdd()
    testHasConsecutiveDigits()
    testAlternatingSum()
    runFreddyFractalViewer()

def main():
    cs112_f21_week9_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()

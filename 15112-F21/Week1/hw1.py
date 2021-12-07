#################################################
# hw1.py
# name: Gaeun Lee
# andrew id: gaeunl
#################################################

import cs112_f21_week1_linter
import math

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

#################################################
# Part A
#################################################

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    distanceBetweenCenters = distance(x1, y1, x2, y2)
    return (distanceBetweenCenters <= (r1 + r2))

def getInRange(x, bound1, bound2):
    lo = min(bound1, bound2)
    hi = max(bound1, bound2)
    if (x < lo): return lo
    elif ( x > hi): return hi
    else: return x

def eggCartons(eggs):
    return math.ceil(eggs/12)

def pascalsTriangleValue(row, col):
    if type(row) != int or type(col) != int:
        return None
    if ((row < 0) or (col < 0) or (col > row)): return None
    if row >= 0 and col == 0:
        return 1
    else:
        return roundHalfUp(math.factorial(row) / (math.factorial(col) 
                        * math.factorial(row-col)))

def getKthDigit(n, k): 
    n = abs(n)
    if type(n) != int or type (k) != int:
        return None
    if k < 0:
        return None
    if k >= 0:
        return math.floor(n//10**k) % 10
    elif n < 10 ** k:
        return 0
    
def setKthDigit(n, k, d):
    if type(k) != int or type(n) != int or type(d) != int:
        return None
    if k < 0 or d < 0 or d > 9:
        return None 
    if n >= 0 and n < 10**k:
        return d*10**k + n
    elif n < 0 and n < 10**k:   
        return n + getKthDigit(n,k) - d
    if n > 0 and k > 0:
        return n - (getKthDigit(n,k) * 10 ** k) + (d * 10 ** k)
    elif n < 0 and k > 0:
        return n + (getKthDigit(n,k) * 10 ** k) - (d * 10 ** k)
    if n > 0 and k == 0:
        return n - getKthDigit(n,k) + d
    elif n < 0 and k == 0:
        return n + getKthDigit(n,k) - d  


#################################################
# Part B
#################################################
        
def nearestOdd(n):
    if type(n) != int and type(n) != float:
        return None
    if type (n) == int and n % 2 == 1:
        return n
    elif type (n) == int and n % 2 ==0:
        return n - 1
    elif (type(n) == float) and ( n % 2 != 0.0):
        return int(roundHalfUp(n // 2 * 2 + 1))
    elif (type(n) == float) and (n % 2 == 0.0):
        return int(n - 1)

    
def numberOfPoolBalls(rows):
    if rows < 0:
        return None
    elif rows >= 0 or rows == int:
        return rows * (rows + 1) / 2
    

def numberOfPoolBallRows(balls):
    if balls < 0:
        return None
    elif balls == 0:
        return 0
    elif balls > 0 or balls == int:
        return math.ceil(math.sqrt(2 * balls + 0.25) -0.5)
        

def colorBlender(rgb1, rgb2, midpoints, n):
    if n < 0 or n > midpoints+1:
        return None
    if n == 0:
        return rgb1

    rgb1_red = rgb1 // 1000000
    rgb1_green = (rgb1 - (rgb1_red * 1000000)) // 1000
    rgb1_blue = rgb1 - (rgb1_red * 1000000 + rgb1_green * 1000)

    rgb2_red = rgb2 // 1000000
    rgb2_green = (rgb2 - (rgb2_red * 1000000)) // 1000
    rgb2_blue = rgb2 - (rgb2_red * 1000000 + rgb2_green * 1000)

    interval_red = (abs(rgb1_red - rgb2_red) / (midpoints + 1))
    interval_green = (abs(rgb1_green - rgb2_green) / (midpoints + 1))
    interval_blue = (abs(rgb1_blue - rgb2_blue) / (midpoints + 1))

    if rgb1_red < rgb2_red:
        result_red = rgb1_red + interval_red * n
    elif rgb1_red > rgb2_red:
        result_red = rgb1_red - interval_red * n
    if rgb1_green < rgb2_green:
        result_green = rgb1_green + interval_green * n
    elif rgb1_green > rgb2_green:
        result_green = rgb1_green - interval_green * n    
    if rgb1_blue < rgb2_blue:
        result_blue = rgb1_blue + interval_blue * n
    elif rgb1_blue > rgb2_blue:
        result_blue = rgb1_blue - interval_blue * n
    
    if result_red - math.floor(result_red) >= 0.5:
        result_red = math.ceil(result_red)
    else:
        result_red = math.floor(result_red)
    if result_green - math.floor(result_green) >= 0.5:
        result_green = math.ceil(result_green)
    else:
        result_green = math.floor(result_green)
    if result_blue - math.floor(result_blue) >= 0.5:
        result_blue = math.ceil(result_blue)
    else:
        result_blue = math.floor(result_blue)

    return result_red * 1000000 + result_green * 1000 + result_blue
    


#################################################
# Bonus/Optional
#################################################

def handToDice(hand):
    if hand < 111 or hand > 666:
        return None
    if hand != int:
        return None
    first_number = hand // 100
    second_number = (hand - first_number * 100) // 10
    third_number = (hand - first_number * 100 - second_number * 10) // 1

    return (first_number, second_number, third_number)
    
def diceToOrderedHand(a,b,c):
    if a != int or b != int or c != int:
        return None
    if a < 1 or a > 6 or b < 1 or b > 6 or c < 1 or c > 6:
        return None
    biggest = max(a,b,c)
    smallest = min(a,b,c)
    middle = (a+b+c) - (biggest+smallest)
    if biggest == smallest:
        return 100 * a + 10 * b + c
    if biggest == middle:
        return biggest * 100 + middle * 10 + smallest
    return biggest * 100 + middle * 10 + smallest 

def playStep2(hand, dice):
    if hand > 666 or hand < 111:
        return None
    if hand != int and dice != int:
        return None
    
    if max(handToDice(hand)) == min(handToDice(hand)):
        return (hand, dice)
     
    first_number = hand // 100
    second_number = (hand - first_number * 100) // 10
    third_number = (hand - first_number * 100 - second_number * 10) // 1

    middle = (first_number + second_number + third_number) - (max(first_number, 
            second_number, third_number) + min(first_number,second_number, 
            third_number))
    
    if max(handToDice(hand)) == middle:
        return (diceToOrderedHand(dice%10, max(handToDice(hand), middle)), 
                dice // 10)
    
    if min(handToDice(hand)) == middle:
        return (diceToOrderedHand(dice%10, min(handToDice(hand), middle)),
                dice // 10)

    if max(handToDice(hand)) != middle != min(handToDice(hand)):
        return diceToOrderedHand(dice % 10, dice // 10 % 10, 
                max(handToDice(hand)), dice // 100
    
    

def score(hand):

    

            

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testGetKthDigit()
    testSetKthDigit()
    # Part B:
    testNearestOdd()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testColorBlender()
    # Bonus:
    # testBonusPlayThreeDiceYahtzee()
    # testBonusFindIntRootsOfCubic()

def main():
    cs112_f21_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()

#################################################
# hw4.py
# name: Gaeun Lee
# andrew id: gaeunl
#################################################

import cs112_f21_week4_linter
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

def alternatingSum(L):
    result = 0
    for i in range(len(L)):
        if i % 2 ==0: #when the index is even, add the value
            result += L[i]
        else:
            result -= L[i] #when odd, substract the value
    return result

def median(L):
    K = sorted(L)
    if not type(K) == list or K == []:
        return None
     #non-destructive way
    value = len(K)//2
    if len(K) % 2 == 0: #when len(K) is even, get the average of 2 middle values
        return (K[value-1] + K[value])/2 
    else:
        return K[value] #when odd, just the middle value

def smallestDifference(L):
    best = 10**100 #set a large number
    if L == []: return -1
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            difference = abs(L[i]-L[j]) #loop through to substract every value
            if difference < best:
                best = difference 
    return best

def nondestructiveRemoveRepeats(L):
    value = [] #store values in another place
    for i in L:
        if i not in value:
            value.append(i)
    return value

def destructiveRemoveRepeats(L):
    i = 0
    while i < len(L):
        if L[i] in L[:i]:
            L.pop(i) #destructive method
        else:
            i += 1
    
#################################################
# Part B
#################################################

def isSorted(L):
    if len(L) <= 1:
        return True 
    checkValue = True 
    #two 'for' loops for ascending and descending orders respectively.
    for i in range(len(L)-1):  #ascending first
        if L[i+1] < L[i]: #L[i+1] should be bigger than L[i] if ascending
            checkValue = False 
            break 
    if checkValue == True:
        return checkValue
    else:
        checkValue = True #reset the checkValue from False to True
    for i in range(len(L)-1): #descending
        if L[i+1] > L[i]: 
            checkValue = False
            break
    return checkValue

def lookAndSay(L):
    K=copy.copy(L) #non-destructive
    if K == []: return []
    result=[]
    #Add tuples in result: goal -> print (K[0].count, K[0])
    count = 1
    current = K.pop(0) 
    for number in K:
        if number == current:
            count += 1
        else: #if the number is not a currentvalue
            result.append((count, current))
            count = 1 #reset the count
            current = number #store the number to the currentvalue 
    result.append((count, number)) #for the previous 'if' statement
    return result

    #we need to remove K[0] and keep going with the for loop
    #pop or remove method (but here pop is more appropriate (index))
    #as we examine numbers in order, we can say current = K.pop[0]

def inverseLookAndSay(L):
    K = copy.copy(L)
    if K == []: return []
    result = []
    for value in K: #inside tuple, count = tuple[0], number = tuple[1]
        count = value[0] #each tuple is considered with index 0 and 1
        number = value[1]
        for i in range(count):
            result.append(number) #add numbers altogether in a list
    return result

def multiplyPolynomials(p1, p2):
    #group terms together(pattern: (len(p1)+len(p2)-1) )
    sum = [0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            sum[i+j] += p1[i]*p2[j] #sum[i+j] represents the nth term
    return sum

def bestScrabbleScore(dictionary, letterScores, hand):
    bestLetter = ""
    bestScore = 0
    for letter in dictionary: #each letter
        if isHandinDictionary(hand, letter) == True:
            score = sumScrabbleScores(letter, letterScores)
            currentLetter = letter
            if score > bestScore:
                bestScore = score #store the bestScore 
                bestLetter = currentLetter #also store the bestLetter for result
            elif score == bestScore:
                if isinstance(bestLetter, list):
                    bestLetter.append(letter)
                else: #if str or int:
                    bestLetter = [bestLetter, letter]
    result = (bestLetter, bestScore)
    if bestScore == 0: 
        return None
    return result

def isHandinDictionary(hand, dictionary): #letter from dictionary
    #see if hands have all the letters in dictionary
    for number in range(97, 123): #ord('a') to ord('z')
        if hand.count(chr(number)) < dictionary.count(chr(number)):
            return False #dictionary must always have smaller/equal # of letters
    return True

def sumScrabbleScores(value, letterScores):
    #sum the values of the chosen word from the dictionary based on letterScores
    sum = 0
    for number in value:
        index = ord(number) - ord('a')
        sum += letterScores[index]
    return sum

#################################################
# Bonus/Optional
#################################################

def linearRegression(pointsList):
    return 42

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def _verifyAlternatingSumIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    alternatingSum(a)
    return (a == b)

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(_verifyAlternatingSumIsNondestructive())
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed!')

def _verifyMedianIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    median(a)
    return (a == b)

def testMedian():
    print('Testing median()...', end='')
    assert(_verifyMedianIsNondestructive())
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed!')

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = a + [ ] # copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed!")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed!")

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

#def _verifyLookAndSayIsNondestructive():
   # a = [1,2,3]
   # b = a + [ ] # copy.copy(a)
    
    #lookAndSay(a) # ignore result, just checking for destructiveness here
   # return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    #assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    

    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = a + [ ] # copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]

    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testAlternatingSum()
    testMedian()
    testSmallestDifference()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()
    # Part B:
    testLookAndSay()
    testBestScrabbleScore()
    testInverseLookAndSay()
    testMultiplyPolynomials()
    testIsSorted()
    
    # Bonus:
    #testLinearRegression()
    #testRunSimpleProgram() 

    

def main():
    cs112_f21_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()

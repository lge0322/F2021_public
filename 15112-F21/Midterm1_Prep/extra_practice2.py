#################################################
# extra_practice2.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f21_week2_linter
import math
from tkinter import *

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
################################################

def nthLeftTruncatablePrime(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isLeftTruncatablePrime(n):
            found += 1
    print(guess)
    return guess

def isLeftTruncatablePrime(n):
    while n > 0:
        digit = n % 10**numberOfDigit(n)
        n = n - (digit * (10**numberOfDigit(n)))
        if digit == 0: return False
        if not isPrime(n): return False
    return True

def numberOfDigit(n):
    count = 0
    while n > 0:
        count +=1
        n //= 10

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True
    

def nthPowerfulNumber(n):
    return 42

def nthWithProperty309(n):
    return 42

def longestIncreasingRun(n):
    return 42

def nthCarolPrime(n):
    return 42

def nthPerfectNumber(n):
    return 42

def sumOfSquaresOfDigits(n):
    return 42

def isHappyNumber(n):
    return 42

def nthHappyNumber(n):
    return 42

def isHappyPrime(n):
    return 42

def nthHappyPrime(n):
    return 42

def isSemiPrime(n):
    return 42

def pi(n):
    return 42

def h(n):
    return 42

def estimatedPi(n):
    return 42

def estimatedPiError(n):
    return 42

#################################################
# Test Functions
#################################################

def testNthLeftTruncatablePrime():
    print('Testing nthLeftTruncatablePrime()... ', end='')
    assert(nthLeftTruncatablePrime(0) == 2)
    assert(nthLeftTruncatablePrime(10) == 53)
    assert(nthLeftTruncatablePrime(1) == 3)
    assert(nthLeftTruncatablePrime(5) == 17)
    print('Passed!')

def testNthPowerfulNumber():
    print('Testing nthPowerfulNumber()... ', end='')
    assert(nthPowerfulNumber(0) == 1)
    assert(nthPowerfulNumber(1) == 4)
    assert(nthPowerfulNumber(2) == 8)
    assert(nthPowerfulNumber(3) == 9)
    assert(nthPowerfulNumber(4) == 16)
    assert(nthPowerfulNumber(5) == 25)
    assert(nthPowerfulNumber(10) == 64)
    assert(nthPowerfulNumber(15) == 121)
    assert(nthPowerfulNumber(20) == 196)
    print('Passed!')

def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(1) == 418)
    assert(nthWithProperty309(2) == 462)
    assert(nthWithProperty309(3) == 474)
    print("Passed!")

def testLongestIncreasingRun():
    print('Testing longestIncreasingRun()... ', end='')
    assert(longestIncreasingRun(27648923679) == 23679)
    assert(longestIncreasingRun(123345) == 345)
    assert(longestIncreasingRun(1232) == 123)
    assert(longestIncreasingRun(0) == 0)
    assert(longestIncreasingRun(1) == 1)
    assert(longestIncreasingRun(10012301230123) == 123)
    assert(longestIncreasingRun(12345678987654321) == 123456789)
    print('Passed!')

def testNthCarolPrime():
    print('Testing nthCarolPrime()... ', end='')
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(6) == 16769023)
    print('Passed!')

def testNthPerfectNumber():
    print('Testing nthPerfectNumber()... ', end='')
    assert(nthPerfectNumber(0) == 6)
    assert(nthPerfectNumber(1) == 28)
    assert(nthPerfectNumber(2) == 496)  
    assert(nthPerfectNumber(3) == 8128) # this can be slow 
    print('Passed!')

def testSumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
    assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
    assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4+9+16 = 29
    print("Passed!")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed!")

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    print("Passed!")

def testIsHappyPrime():
    print("Testing isHappyPrime()...", end="")
    assert(isHappyPrime(1) == False)
    assert(isHappyPrime(2) == False)
    assert(isHappyPrime(3) == False)
    assert(isHappyPrime(7) == True)
    assert(isHappyPrime(10) == False)
    assert(isHappyNumber(13) == True)
    print("Passed!")

def testNthHappyPrime():
    print("Testing nthHappyPrime...", end="")
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(10) == 167)
    assert(nthHappyPrime(20) == 397)
    print("Passed!")

def testHappyPrimes():
    testSumOfSquaresOfDigits()
    testNthHappyNumber()
    testIsHappyPrime()
    testNthHappyPrime()

def testIsSemiPrime():
    print('Testing isSemiPrime()...', end='')
    assert(isSemiPrime(14) == True)
    assert(isSemiPrime(65) == True)
    assert(isSemiPrime(18) == False)
    assert(isSemiPrime(1679) == True)
    assert(isSemiPrime(17) == False)
    assert(isSemiPrime(15112) == False)
    assert(isSemiPrime(-26) == False)
    assert(isSemiPrime('foo') == False)
    print('Passed!')

def testPi():
    print('Testing pi()... ', end='')
    assert(pi(1) == 0)
    assert(pi(2) == 1)
    assert(pi(3) == 2)
    assert(pi(4) == 2)
    assert(pi(5) == 3)
    assert(pi(100) == 25)  # there are 25 primes in the range [2,100]
    print('Passed!')

def testH():
    print('Testing h()... ', end='')
    assert(almostEqual(h(0),0))
    assert(almostEqual(h(1),1/1            ))  # h(1) = 1/1
    assert(almostEqual(h(2),1/1 + 1/2      ))  # h(2) = 1/1 + 1/2
    assert(almostEqual(h(3),1/1 + 1/2 + 1/3))  # h(3) = 1/1 + 1/2 + 1/3
    print('Passed!')

def testEstimatedPi():
    print('Testing estimatedPi()... ', end='')
    assert(estimatedPi(100) == 27)
    print('Passed!')

def testEstimatedPiError():
    print('Testing estimatedPi()... ', end='')
    assert(estimatedPiError(100) == 2) # pi(100) = 25, estimatedPi(100) = 27
    assert(estimatedPiError(200) == 0) # pi(200) = 46, estimatedPi(200) = 46
    assert(estimatedPiError(300) == 1) # pi(300) = 62, estimatedPi(300) = 63
    assert(estimatedPiError(400) == 1) # pi(400) = 78, estimatedPi(400) = 79
    assert(estimatedPiError(500) == 1) # pi(500) = 95, estimatedPi(500) = 94
    print('Passed!')

def testPrimeCounting():
    testPi()
    testH()
    testEstimatedPi()
    testEstimatedPiError()

#################################################
# testAll and main
#################################################

def testAll():
    testNthLeftTruncatablePrime()
    testNthPowerfulNumber()
    testNthWithProperty309()
    testLongestIncreasingRun()
    testNthCarolPrime()
    testNthPerfectNumber()
    testHappyPrimes()
    testIsSemiPrime()
    testPrimeCounting()

def main():
    cs112_f21_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
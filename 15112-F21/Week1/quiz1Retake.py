'''
Quiz 1 Retake Part 2
(20 minutes TOTAL for part1+part2)

If you are not being proctored, 
you must CLOSE THIS WINDOW and email the professors immediately.

You may not use LOOPS or STRINGS.

Use VS Code to answer the ONE FR in part 2.  You may not return to part 1.
-DO NOT leave VS Code until you are done with part2 or your proctor tells you 
  to.  You must IMMEDIATELY submit after leaving VS Code.

-If you encounter a tech fail (like if laptop internet cuts out), private chat 
the TA or faculty member on duty

'''

##################################
# FR [60 pts]
##################################

'''
Background: isSeesaw(n)

A number is a seesaw number (a coined term) if it has four digits total, 
with two consecutive even  digits and two consecutive odd digits. 

For example, 2233, 7524, and -6879 are all seesaw numbers because they have 
two consecutive even digits, two consecutive odd digits, and they are a four
digit number. 

Write the function isSeesaw(n) that takes in a value n that may or may 
not be an integer and returns True is the number is a seesaw number and 
False otherwise. Do not crash if a non-integer number is not passed in! 

'''

# write the function here!

def testIsSeesaw(n):
    if (not isinstance (n, int)):
        return False
    n = abs(n)
    if n < 1000 or n > 9999:
        return False
    ones = n % 10
    tens = n // 10 % 10
    hundreds = n // 100 % 10
    thousands = n // 1000
    mod_ones = ones % 2
    mod_tens = tens % 2
    mod_hundreds = hundreds % 2
    mod_thousands = thousands % 2
    if (mod_ones == 0) and (mod_tens == 0) and (mod_hundreds == 1) and (
        mod_thousands == 1):
        return True
    elif (mod_ones == 1) and (mod_tens == 1) and (mod_hundreds == 0) and (
        mod_thousands == 0):
        return True
    else:
        return False

# test cases! 
def testIsSeesaw():
    print("testing....")
    assert(isSeesaw(-2233) == True)
    assert(isSeesaw(5687) == False)
    assert(isSeesaw(8920) == False)
    assert(isSeesaw('3322') == False)
    assert(isSeesaw(5946) == True)
    assert(isSeesaw(2233.0) == False)
    assert(isSeesaw(33) == False)
    print('passed!')

#################################################
# hw8.py:
#
# Your name: Gaeun Lee
# Your andrew id: gaeunl
#################################################

import cs112_f21_week8_linter
from cmu_112_graphics import *

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
# Midterm1 Free Responses
#################################################

def firstNAcceptedValues(n, rules):
    found = [] #should be a list containing N values
    guess = 1
    while len(found) < n:
        if isAcceptedValues(guess, rules):
            found.append(guess)
        guess += 1
    return found

def isAcceptedValues(value, rules): #credit for midterm solution session!
    for line in rules: #get a statement
        values = line.split() #each noun
        if '%' in line:
            factor = int(values[0][2:]) #number after %
            xValue = value % factor
        else:
            xValue = value

        findEqual = int(values[-1]) #now check if xValue should be equal or not
        
        if line.count('equal') == 1:
            acceptedValue = (xValue == findEqual) #give a boolean value

        else: #multiple
            acceptedValue = (xValue % findEqual == 0)

        if 'not' in line: #not equal
            acceptedValue = not acceptedValue
        if not acceptedValue: #if not true
            return False
    return True

from dataclasses import make_dataclass

Dot = make_dataclass('Dot', ['cx', 'cy', 'r', 'dx', 'dy', 'color'])

def appStarted(app):
    app.dots = []

import random

#credit for midterm solution session!

def mousePressed(app, event):
    isClicked = False #to check if the dot is clicked by the user
    for i in range(len(app.dots)):
        if (distance(event.x, event.y, app.dots[i].cx, app.dots[i].cy) 
                    < app.dots[i].r): #check if the click is within the radius
            if app.dots[i].color == 'red': #if paused, then release the dot
                app.dots[i].color = 'green'
            else:
                app.dots[i].color = 'red'
            isClicked = True
    if isClicked == False:
        newDot = Dot(event.x, event.y, 20, random.randint(-3, 3), 
                    random.randint(-3,3),'green')
        app.dots.append(newDot)

import math

def distance(x0, y0, x1, y1): 
    return math.sqrt((x0 -x1) ** 2 + (y0 - y1) ** 2)

def timerFired(app):
    i = 0
    while i < len(app.dots):
        if app.dots[i].color == 'green': #if green, keep going
            app.dots[i].cx += app.dots[i].dx
            app.dots[i].cy += app.dots[i].dy
        if (app.dots[i].cx < 0 or app.dots[i].cx > app.width or 
            app.dots[i].cy  < 0 or app.dots[i].cy > app.height):
            app.dots.pop(i) #if out of the screen, remove the dots
        else:
            i += 1 

def redrawAll(app, canvas):
    canvas.create_text(app.width//2, 15,
                       text=f'{len(app.dots)} Dot(s)', font='Arial 30 bold')
    for dot in app.dots:
        canvas.create_oval(dot.cx-dot.r, dot.cy-dot.r, dot.cx+dot.r,
                            dot.cy+dot.r, fill = dot.color)
def midterm1Animation():
    runApp(width=400, height=400)

#################################################
# Other Classes and Functions for you to write
#################################################

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = [] 
        self.getFriendName = [] #store the values

    def __eq__(self, other):
        return isinstance(other, Person) #see if other is also within the class
    
    def getName(self): 
        return self.name #get name
    
    def getAge(self):
        return self.age #get age

    def getFriends(self):
        return self.friends #get friends by adding friends' names
    
    def getFriendsNames(self):
        if len(self.getFriendName) > 1: #do not need to sort if len(list) < 2
            self.getFriendName = sorted(self.getFriendName) 
            #sorting names alphabetically
        return self.getFriendName

    def addFriend(self, other):
        if not self.name in other.getFriendName:
            self.getFriendName.append(other.name)
            other.getFriendName.append(self.name) 
            #my friend = the other, the other's friend = myself
            self.friends.append(other)
            other.friends.append(self)

            #if other not in self.friends:
            #self.friends.append(other)
            #other.friends.append(self)
    
    def addFriends(self, other):
        self.friends.append(other)
        for name in other.getFriendName:
            if name not in self.getFriendName: #should not double/triple count
                self.getFriendName.append(name)

        #for friend in other.friends:
        #self.addFriend(friend)

def getPairSum(L, target):
    K = copy.deepcopy(L)
    for i in K: #check each value #O(N)
        minusElement = target - i #O(1)
        K.remove(i) 
        if (minusElement in K): #can't repeat same value
            return (i, minusElement)

def containsPythagoreanTriple(L):
    L.sort() #O(nlogn)
    for i in range(1, len(L)): #O(N)
        a, b = L[i-1] ** 2, L[i] ** 2  #using a**2+b**2 = c**2
        c = (math.sqrt(a+b)) 
        if c in L[i+1:]:
            return True
    return False

def movieAwards(oscarResults):
    res = {}
    value = []
    for movie in oscarResults:
        value.append(movie[1]) #get the list of movies
    for nomination in value:
        res[nomination] = res.get(nomination, 0) + 1 #store the values
    return res

    #for award, movie in oscarResults:
    #if movie in results: result[movie] += 1
    #else: result[movie] = 1

def friendsOfFriends(friends):
    res = {}
    for name in friends:
        me, myFriends = name, friends[name]
        res[me] = reallyFofF(me, myFriends, friends) #store the list of friends
    return res

def reallyFofF(me, myFriends, friends):
    itsFofF = []
    #find my friends first
    for name in myFriends:
        itsFofF += friends[name] #in order to pass ["dino"]
    
    itsFofF = set(itsFofF) #now set it to 'set' for main function

    #Now add my friend's friends
    for friend in myFriends:
        if friend in itsFofF: #cannot double count
            itsFofF.remove(friend)
        if me in itsFofF: #exclude myself too!!!
            itsFofF.remove(me)
    return itsFofF


'''
    fof = dict()
    for person in friends:
        directFriends = friends[person]
        for directFriend in directFriends:
            indirectFriends = friends[directFriend]
            for indirectFriend in indirectFriends
                if indirectFriend != person and indirectFriend not in
                directFriends:
                fof[person].add(indirectFriend)
    return fof
'''

#################################################
# Bonus Animation
#################################################

def bonus_appStarted(app):
    app.counter = 0

def bonus_keyPressed(app, event):
    pass

def bonus_mousePressed(app, event):
    pass

def bonus_timerFired(app):
    app.counter += 1

def bonus_redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'bonusAnimation', font='Arial 30 bold')
    canvas.create_text(app.width-20, app.height-20, text=str(app.counter))

def bonusAnimation():
    runApp(width=400, height=400, fnPrefix='bonus_')

#################################################
# Test Functions
#################################################


def testFirstNAcceptedValues():
    print('Testing firstNAcceptedValues...', end='')
    oneRule = [ 'x must be a multiple of 3' ]
    assert(firstNAcceptedValues(6, oneRule) == [3, 6, 9, 12, 15, 18])
    twoRules = [ 'x must be a multiple of 3',
                 'x must not be a multiple of 9' ]
    assert(firstNAcceptedValues(6, twoRules) == [3, 6, 12, 15, 21, 24])
    fourRules = [ 'x must be a multiple of 3',
                  'x must not be a multiple of 9',
                  'x%2 must be a multiple of 2',
                  'x%10 must not be equal to 4' ]
    assert(firstNAcceptedValues(6, fourRules) == [6, 12, 30, 42, 48, 60])
    print("Passed!")
    

def testMidterm1Animation():
    print('Note: You must visually inspect your midterm1 animation to test it.')
    midterm1Animation()

def testPersonClass():
    print('Testing Person Class...', end='')

    fred = Person('fred', 32)
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    # Note: person.getFriends() returns a list of Person objects who
    #       are the friends of this person, listed in the order that
    #       they were added.
    # Note: person.getFriendNames() returns a list of strings, the
    #       names of the friends of this person.  This list is sorted!
    assert(fred.getFriends() == [ ])
    assert(fred.getFriendsNames() == [ ])

    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == [ ])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    assert(wilma.getFriendsNames() == ['fred'])
    assert(fred.getFriends() == [wilma]) # friends are mutual!
    assert(fred.getFriendsNames() == ['wilma'])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!

    betty = Person('betty', 29)
    fred.addFriend(betty)
    assert(fred.getFriendsNames() == ['betty', 'wilma'])

    pebbles = Person('pebbles', 4)
    betty.addFriend(pebbles)
    assert(betty.getFriendsNames() == ['fred', 'pebbles'])

    barney = Person('barney', 28)
    barney.addFriend(pebbles)
    barney.addFriend(betty)
    barney.addFriends(fred) # add ALL of Fred's friends as Barney's friends
    assert(barney.getFriends() == [pebbles, betty, wilma])
    assert(barney.getFriendsNames() == ['betty', 'pebbles', 'wilma'])
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, betty, barney])
    assert(fred.getFriendsNames() == ['barney', 'betty', 'wilma']) # sorted!
    assert(barney.getFriends() == [pebbles, betty, wilma, fred])
    assert(barney.getFriendsNames() == ['betty', 'fred', 'pebbles', 'wilma'])
    print('Passed!')

def testGetPairSum():
    print("Testing getPairSum()...", end="")
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5,5], 10) == (5, 5))
    assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in
                      [ (10, -8), (-8, 10),(-1, 3), (3, -1), (1, 1) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, 0, 5], 10) in
                      [ (10, 0), (0, 10)] )
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, -9, 5], 10) in
                      [ (19, -9), (-9, 19)] )
    assert(getPairSum([1, 4, 3], 2) == None) # catches reusing values! 1+1...
    print("Passed!")

def testContainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...", end="")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4]) == True)
    assert(containsPythagoreanTriple([1,3,6,2,8,1,4]) == False)
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,728,4])
                                      == True) # 54, 728, 730
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,729,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                6253, 7800, 9997]) == True) # 6253, 7800, 9997
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9998]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9996]) == False)
    print("Passed!")

def testMovieAwards():
    print('Testing movieAwards()...', end='')
    tests = [
      (({ ("Best Picture", "The Shape of Water"), 
          ("Best Actor", "Darkest Hour"),
          ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
          ("Best Director", "The Shape of Water") },),
        { "Darkest Hour" : 1,
          "Three Billboards Outside Ebbing, Missouri" : 1,
          "The Shape of Water" : 2 }),
      (({ ("Best Picture", "Moonlight"),
          ("Best Director", "La La Land"),
          ("Best Actor", "Manchester by the Sea"),
          ("Best Actress", "La La Land") },),
        { "Moonlight" : 1,
          "La La Land" : 2,
          "Manchester by the Sea" : 1 }),
      (({ ("Best Picture", "12 Years a Slave"),
          ("Best Director", "Gravity"),
          ("Best Actor", "Dallas Buyers Club"),
          ("Best Actress", "Blue Jasmine") },),
        { "12 Years a Slave" : 1,
          "Gravity" : 1,
          "Dallas Buyers Club" : 1,
          "Blue Jasmine" : 1 }),
      (({ ("Best Picture", "The King's Speech"),
          ("Best Director", "The King's Speech"),
          ("Best Actor", "The King's Speech") },),
        { "The King's Speech" : 3}),
      (({ ("Best Picture", "Spotlight"), ("Best Director", "The Revenant"),
          ("Best Actor", "The Revenant"), ("Best Actress", "Room"),
          ("Best Supporting Actor", "Bridge of Spies"),
          ("Best Supporting Actress", "The Danish Girl"),
          ("Best Original Screenplay", "Spotlight"),
          ("Best Adapted Screenplay", "The Big Short"),
          ("Best Production Design", "Mad Max: Fury Road"),
          ("Best Cinematography", "The Revenant") },),
        { "Spotlight" : 2,
          "The Revenant" : 3,
          "Room" : 1,
          "Bridge of Spies" : 1,
          "The Danish Girl" : 1,
          "The Big Short" : 1,
          "Mad Max: Fury Road" : 1 }),
       ((set(),), { }),
            ]
    for args,result in tests:
        if (movieAwards(*args) != result):
            print('movieAwards failed:')
            print(args)
            print(result)
            assert(False)
    print('Passed!')

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()
    fof = friendsOfFriends(d)
    assert(fof["fred"] == set(["dino"]))
    assert(fof["wilma"] == set(["barney", "bam-bam"]))
    result = { "fred":set(["dino"]),
               "wilma":set(["barney", "bam-bam"]),
               "betty":set(),
               "barney":set(),
               "dino":set(),
               "bam-bam":set()
             }
    assert(fof == result)
    d = dict()
    #                A    B    C    D     E     F
    d["A"]  = set([      "B",      "D",        "F" ])
    d["B"]  = set([ "A",      "C", "D",  "E",      ])
    d["C"]  = set([                                ])
    d["D"]  = set([      "B",            "E",  "F" ])
    d["E"]  = set([           "C", "D"             ])
    d["F"]  = set([                "D"             ])
    fof = friendsOfFriends(d)
    assert(fof["A"] == set(["C", "E"]))
    assert(fof["B"] == set(["F"]))
    assert(fof["C"] == set([]))
    assert(fof["D"] == set(["A", "C"]))
    assert(fof["E"] == set(["B", "F"]))
    assert(fof["F"] == set(["B", "E"]))
    result = { "A":set(["C", "E"]),
               "B":set(["F"]),
               "C":set([]),
               "D":set(["A", "C"]),
               "E":set(["B", "F"]),
               "F":set(["B", "E"])
              }
    assert(fof == result)
    print("Passed!")

def testBonusAnimation():
    print('Note: You must visually inspect your bonus animation to test it.')
    bonusAnimation()

def testAll():
    testFirstNAcceptedValues()
    #testMidterm1Animation()
    testPersonClass()
    testGetPairSum()
    testContainsPythagoreanTriple()
    testMovieAwards()
    testFriendsOfFriends()
    testBonusAnimation()

#################################################
# main
#################################################

def main():
    cs112_f21_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()

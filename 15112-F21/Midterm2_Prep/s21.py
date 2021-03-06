import copy, math

def makeEdits(M, E):
    K = copy.deepcopy(M)
    for sentence in E:
        words = sentence.split(" ")
        if words.count("row") == 2:
            for num in range(len(words)):
                if words[num] == "row":
                    add = [].append(words[num+1])
                    print(add)
            adding, added = add[0], add[1]
            for i in K[adding]:
                for j in K[added]:
                    K[added][j] += K[adding][i]
        else:
            for num in range(len(words)):
                if words[num].isdigit: addValue = words[num]
                if words[num] == "col":
                    value = words[num+1]
                    for row in range(len(M)):
                        K[row][value] += addValue
    return K
        

def testMakeEdits():
    print('Testing makeEdits()...', end='')
    M = [ [ 1, 2, 3 ],
          [ 4, 5, 6 ],
          [ 7, 8, 9 ] ]
    E = [ 'add row 0 to row 1',
          'add 10 to col 0',
          'add row 2 to row 0',
        ]
    N = [ [ 28, 10, 12 ],
          [ 15,  7,  9 ],
          [ 17,  8,  9 ] ]
    assert(makeEdits(M, E) == N)
    print('Passed!')

#testMakeEdits()

class Scoreboard(object):
    def __init__(self, scores):
        #Finish writing this class
        self.scores = scores

    def getScore(self, name):
        if name in self.scores:
            return self.scores[name]
        else:
            return None

    def leaders(self):
        res = set()
        best = ""
        bestScore = 0
        for name in self.scores:
            curScore = self.scores[name]
            if curScore > bestScore:
                best = name
                bestScore = curScore
            
            elif curScore == bestScore:
                best = [best] + [name]
        if type(best) != str and len(best) > 1:
            for i in range(len(best)):
                res.add(best[i])
        else:
            res.add(best)
        print(res)
        return res
    def addScore(self, name, point):
        if name in self.scores:
            self.scores[name] += point
        else:
            self.scores[name] = point

    def getAll(self):
        return self.scores

    def getCopy(self):
        k = copy.deepcopy(self.scores)
        return Scoreboard(k)
    
def testScoreboardClass():
    print('Testing Scoreboard class...', end='')
    # Create a Scoreboard with these initial scores
    sb1 = Scoreboard({'Alice':3, 'Bob':4})
    assert(sb1.getScore('Alice') == 3)
    assert(sb1.getScore('Bob') == 4)
    assert(sb1.getScore('Cal') == None)
    assert(sb1.leaders() == { 'Bob' }) # A set of all the leaders

    sb1.addScore('Alice', 2) # Alice just scored 2 points!
    assert(sb1.getScore('Alice') == 5) # Now she has 5 points
    assert(sb1.leaders() == { 'Alice' }) # Alice has 5, Bob has 4

    sb1.addScore('Cal', 2)   # Cal wasn't there, now Cal is, with 2 points
    assert(sb1.getScore('Cal') == 2)
    sb1.addScore('Cal', 3)
    assert(sb1.getScore('Cal') == 5)
    assert(sb1.leaders() == { 'Alice', 'Cal' }) # Alice and Cal both have 5

    assert(sb1.getAll() == { 'Alice':5, 'Bob':4, 'Cal':5 })

    sb2 = sb1.getCopy() # This is a copy of sb1, where changes to the copy
                        # do not affect the original, and vice versa
    assert(sb2.getAll() == { 'Alice':5, 'Bob':4, 'Cal':5 })
    sb2.addScore('Bob', 3) # Bob now has 7 in sb2, but still has only 4 in sb1
    assert(sb2.leaders() == { 'Bob' })
    assert(sb1.leaders() == { 'Alice', 'Cal' })
    print('Passed!')

testScoreboardClass()


def evensAreSorted(L):
    return helper(L, 0)

def helper(L, compare):
    if L ==[]: 
        return True

    else:
        if L[0] % 2 == 1:
            return helper(L[1:], compare)
        else:
            if L[0] <= compare:
                return False
            else:
                return helper(L[1:], L[0])
            

def testEvensAreSorted():
    print('Testing evensAreSorted()...', end='')
    assert(evensAreSorted([2, 4, 8]) == True)
    assert(evensAreSorted([1, 2, 3, 4, 5, 8]) == True)
    assert(evensAreSorted([4, 2, 4, 2, 4]) == False)
    assert(evensAreSorted([1,2,3,3,2,1]) == False)
    assert(evensAreSorted([42, 33, 10, 80]) == False)
    assert(evensAreSorted([4]) == True)
    assert(evensAreSorted([9]) == True)
    assert(evensAreSorted([]) == True)

    print('Passed!')

testEvensAreSorted()

def makeWordLadder(L):
    return makeWordLadderSolver(L, [])

def makeWordLadderSolver(L, res):
    if L == []: 
        return res
    else:
        for i in range(len(L)-1):
            cur = L[i]
            next = L[i+1]
            if cur[-1] == next[0]:
                print(res)
                solution = makeWordLadderSolver(L[1:], res)
                if solution != None:
                    res.append(cur)
                    res.append(next)
                    return solution
                else:
                    res.remove(next)
                    return makeWordLadderSolver(L[1:], res)
    return None
            

def testMakeWordLadder():
    print('Testing makeWordLadder()...', end='')
    assert(makeWordLadder(['aba', 'ca' ,'aa']) in [['ca', 'aba', 'aa'],
                                                  ['ca', 'aa', 'aba']])
    assert(makeWordLadder(['efg', 'abc', 'ghi', 'cde']) 
                                              == ['abc', 'cde', 'efg', 'ghi'])
    assert(makeWordLadder(['a', 'at', 'a', 'xa', 'a']) 
                                              == ['xa', 'a', 'a', 'a', 'at'])
    assert(makeWordLadder(['ab', 'cu', 'bu']) == None)
    assert(makeWordLadder(['abc']) == ['abc'])
    assert(makeWordLadder([]) == [])
    print('Passed!')

testMakeWordLadder()


import copy
def ct1(n):
    M = [list(range(n)), list(range(n,0,-1))]
    P = M
    Q = copy.copy(M)
    R = copy.deepcopy(M)
    M[0][0] = n+1
    P[1] = n+2
    Q[0].reverse()
    R.pop()
    return [P, Q, R]
print(ct1(2)) # careful with brackets and commas!

def ct2(d):
    s, t, u = set(), set(), set()
    for k in d:
        s.add(k)
        for v in d[k]:
            if v%2 == 0:
                t.add(v)
            else:
                u.add(v)
    return { min(s):t, max(s):u }
print(ct2({ 3:[1,2,4,1], 1:[5,5], 2:[0,5] }))

def ct3(n):
    if (n == 0):
        return (0, 1)
    else:
        x, y = ct3(n//10)
        if (n%2 == 0):
            return (x + (n%10), y)
        else:
            return (x, y * (n%10))
print(ct3(324508))

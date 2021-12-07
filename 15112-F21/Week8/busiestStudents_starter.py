def busiestStudents(rosters):
    newDict = dict()
    for course in rosters:
        students = rosters[course]
        for student in students:
            newDict[student] = newDict.get(student, 0) + 1
    
    #best template, find the students with the most number of classes

    bestStudents = set()
    bestClassNum = 0
    for student in newDict:
        curCourses = newDict[student]
        if curCourses > bestClassNum:
            bestClassNum = curCourses
            bestStudents = {student}
        elif curCourses == bestClassNum:
            bestStudents.add(student)
    return bestStudents


def testBusiestStudents():
    print('Testing busiestStudents()...', end='')
    rosters = {
        '15-112':{'amy','bob','claire','dan'},
        '18-100':{'amy','claire','john','mark'},
        '21-127':{'claire','john','zach'},
        '76-101':{'bob','john','margaret'},
    }
    assert(busiestStudents(rosters) == { 'claire', 'john' })
    print('Passed!')

testBusiestStudents()


'''
Write the function findTriplets(L) that takes as input a list L of integers of 
length N and returns a set of all triplets in the list whose sum is equal to 0. 
For example, if the given list is [-1, 0, -3, 2, 1], you should return 
{(1, 0, -1), (-3, 2, 1)} (or any permutation of those numbers). 
If there is no valid triplet, you should return the empty set.
 You may assume that L is a list containing only integers. 
 The "naive" solution would use 3 loops to check all triplets of values in L. 
 You should use sets and/or dictionaries to do this in a faster way.
'''

def testFindTriplets():
    print('Testing Find Triplets....')
    assert(findTriplets([-1, 0, -3, 2, 1]) == {(1, 0, -1), (-3, 2, 1)})
    assert(findTriplets([-7, 4, 5, 2, 3, -5, 0, 3]) == {-7, 2, 5})



'''
Write the function mostCommonName, that takes a list of names 
(such as ["Jane", "Aaron", "Cindy", "Aaron"], and returns 
the most common name in this list (in this case, "Aaron"). 
If there is more than one such name, return a set of the most common names. 
So mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) returns the set 
{"Aaron", "Jane"}. If the set is empty, return None. Also, treat names case 
sensitively, so "Jane" and "JANE" are different names. You should write
 three different versions, one that runs in O(n**2), O(nlogn) and O(n).'''

import copy 

def mostCommonName(L):
    K = copy.deepcopy(L)
    bestName = ""
    bestCount = 0
    for name in K:
        count = L.count(name)
        if count > bestCount:
            bestCount = count
            bestName = name
            print(bestName)
        elif count == bestCount:
            bestName = bestName + ' ' + name
            while K.count(name) > 1:
                K.remove(name)
    print(bestName)
    return bestName
        
def testMostCommonName():
    print("Testing mostCommonName()...", end="")
    assert(mostCommonName(["Jane", "Aaron", "Cindy", "Aaron"])
           == "Aaron")
    assert(mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])
           == {"Aaron", "Jane"})
    assert(mostCommonName(["Cindy"]) == "Cindy")
    assert(mostCommonName(["Jane", "Aaron", "Cindy"])
           == {"Aaron", "Cindy", "Jane"})
    assert(mostCommonName([]) == None)
    print("Passed!")

testMostCommonName()

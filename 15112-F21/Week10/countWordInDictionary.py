import os

def readFile(path):
    with open(path, "r") as f:
        txt = f.read()
    return txt

def countWordInDirectory(path, word):   
    if os.path.isfile(path):
        return countWordInText(path, word)
    else:
        total = 0
        for elem in os.listdir(path): #see if it's a folder
            newPath = path+"/"+elem
            total += countWordInDirectory(newPath, word)
        return total
                               
def countWordInText(text, word):
    if text == []: return 0
    if text[0] == word:
        return countWordInText(text[1:], word)+1
    else:
        return countWordInText(text[1:], word)
        
        

def testCountWordInDirectory():
    print("Testing countWordInDirectory...", end="")
    assert(countWordInDirectory("FileProblemsFolder", "class") == 5)
    assert(countWordInDirectory("FileProblemsFolder", "case") == 3)
    assert(countWordInDirectory("FileProblemsFolder", "kosbie") == 0)
    assert(countWordInDirectory("FileProblemsFolder", "fox") == 1)
    assert(countWordInDirectory("FileProblemsFolder", "quince") == 0)
    print("Passed!")

testCountWordInDirectory()

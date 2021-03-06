import copy
def ct2(L, i):
  M = L
  N = copy.copy(L)
  L.append(i)
  M = M + [i-1]
  N[0] = i
  return (L, M, N)
print(ct2([1], 4))
'''
def ct1(d):
  s = set()
  for k in d:
    if k in d[k]:
      s.add(max(d[k]) % k)
  return s

print(ct1(
      { 2: { 3, 6 },
        4: { 2, 4, 7 },
        5: { },
        6: { 1, 6, 8 },
        8: { 1, 8, 82 },
      }))
'''

class A(object):
    def __init__(self, x, y):
            self.x = x
            self.y = y
    def f(self):
            return self.x + self.y
    def g(self):
            return self.f()/10

class B(A):
    def __init__(self, x):
            super().__init__(x, x**2)
    def g(self):
            return self.f()*10

def ct1(x):
    a = A(x, 2*x)
    b = B(x)
    print( [ a.g(), b.g() ] )

ct1(4)

def f(n):
        # note: f(n) returns a string
        s = str(n)
        if (n < 2):
            return ('a' + s)
        elif (n % 5 == 0):
            return ('b' + s)
        else:
            return f(n//2) + ('c' + s) + f(n//4)

print(f(11))

def islands(L):
    if len(L) < 3: return []
    return islandsHelper(L, L[0], L[1], [])

def islandsHelper(L, cur, next, res):
    if L == []: return res
    else:
        if cur % 2 != next % 2:
            res.append(cur)
            result = islandsHelper(L[1:], L[0], L[1], res)
            if result!= None:
                return result
            res.move(cur)
    return None
    

def testIslands():
        print('Testing islands()...', end='')
        assert(islands([ ]) == [ ])
        assert(islands([1, 2, 3]) == [ 2 ])
        assert(islands([1, 2, 4]) == [ ])
        assert(islands([1, 2]) == [ ])
        assert(islands([1, 2, 3, 5, 6, 7, 8, 10, 9]) == [ 2, 6, 7])
        print('Passed!')

#testIslands()
  

class File(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return f'File(name={self.name},size={self.size})'

    def copyFile(self, file):
        return File(file, self.size)

class Folder(File):
    def __init__(self, name):
        self.name = name
        self.fileCount = 0
        self.size = 0
    
    def __repr__(self):
        return f'Folder(name={self.name},fileCount={self.fileCount})'

    def add(self, file):
        self.fileCount += 1
        self.size += file.size
        if isinstance(file, Folder):
            self.fileCount -=1
        

    def getTotalFileSize(self):
        return self.size
        
    

        
def testFilesAndFolders():
        print('Testing File and Folder classes...', end='')

        foo = File('foo.txt', 25)
        print(str(foo))
        assert(str(foo) == 'File(name=foo.txt,size=25)')

        folderA = Folder('A')
        assert(str(folderA) == 'Folder(name=A,fileCount=0)')

        folderA.add(foo)
        assert(str(folderA) == 'Folder(name=A,fileCount=1)')

        folderB = Folder('B')
        assert(str(folderB) == 'Folder(name=B,fileCount=0)')

        bar1 = File('bar1.txt', 100)
        assert(str(bar1) == 'File(name=bar1.txt,size=100)')
        bar2 = bar1.copyFile('bar2.txt')
        assert(str(bar2) == 'File(name=bar2.txt,size=100)')

        folderB.add(bar1)
        assert(str(folderB) == 'Folder(name=B,fileCount=1)')
        folderB.add(bar2)
        assert(str(folderB) == 'Folder(name=B,fileCount=2)')

        # The fileCount only counts files, not folder, and does
        # so only for files in this folder and not in any folders
        # within this folder.  Thus, when we add folderB to folderA,
        # it does not increase the fileCount of folderA
        folderA.add(folderB)
        print(str(folderA))
        assert(str(folderA) == 'Folder(name=A,fileCount=1)')

        # folder.getTotalFileSize() returns the sum of the sizes of
        # all the files in that folder plus all the sizes of files in
        # any folder recursively within that folder.
        # To do this, you must write getTotalFileSize() recursively

        # folderB contains 2 files each of size 100, so that's 200
        assert(folderB.getTotalFileSize() == 200)
        # folderA contains 1 file of size 25, but also contains
        # folderB which is of size 200, so that's 225 in total
        assert(folderA.getTotalFileSize() == 225)

        bar3 = bar2.copyFile('bar3.txt')
        folderB.add(bar3)
        # A new file was added to folderB, which is in folderA
        # Accordingly, the total file size of folderA has increased to 325
        assert(folderA.getTotalFileSize() == 325)
        print('Passed!')

testFilesAndFolders()
  
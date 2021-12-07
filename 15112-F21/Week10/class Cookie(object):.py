
def vmc(L):
    res = set()
    for value in L:
        if L.count(value) == value:
            res.add(value)
    return res

def testvalues():

    assert(vmc([1, 2, 3, 4, 5]) == {1})
    assert(vmc([1, 5, 1, 1, 2]) == set())
    assert(vmc([5, 2, 5, 2, 5, 6, 5, 1, 5, 0]) == {1, 2, 5})
    print('passed!')
testvalues()


def isPrime(n):
    if n < 2: return False
    elif n == 2: return True
    else:
        maxFactor = round(n**0.5)
        for i in range(2, maxFactor+1):
            if n % i == 0: return False
        return True

def onlyPrimes(L):
    if L == []: return L
    else:
        cur = L[0]
        next = onlyPrimes(L[1:])
        if isPrime(cur):
            print(cur)
            return [cur]+next
    return next

def kSuperSplit(L, k, n):
    

def testPrimes():
    assert(onlyPrimes([]) == [])
    assert(onlyPrimes([1, 5, 1, 1, 2]) == [5, 2])
    assert(onlyPrimes([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7])
testPrimes()
class File(object):
    def __init__(self,name,size):
        self.name = name
        self.size = size
    
    def getSize(self):
        return self.size

    def __repr__(self):
        return f'File("{self.name}", {self.size})'
def testFileFolder():
 print("Testing File, Python File and Folder...", end="")
 a = File("A", 15)
 b = File("B", 1)
 c = File("C", 12)
 assert(a.getSize() == 15)
 assert(a == File("A", 15))
 assert(a != File("A", 16))
 assert(a != File("B", 15))
 assert(a != "Don't Crash Here")
 assert(str([b, c]) == "[File('B', 1), File('C', 12)]")
 # Hint: do not write more methods than you need to...
 h = PythonFile("Hi", 100)
 assert(isinstance(h, File))
 assert(not isinstance(a, PythonFile))
 assert(h.getSize() == 100)
 assert(repr(h) == PythonFile('Hi', 100))
 # Running a Python file always outputs the string "Hello World!"
 assert(h.runFile() == "Hello World!")
 # These work just like actual files and folders...
 F0 = Folder([])
 F1 = Folder([a, F0])
 F2 = Folder([F1])
 F3 = Folder([b, h])
 F4 = Folder([F2, c, F3])
 # Hint: this method is recursive...
 assert(F0.getFileNames() == set())
 assert(F1.getFileNames() == {"A"})
 assert(F2.getFileNames() == {"A"})
 assert(F3.getFileNames() == {"B", "Hi"})
 assert(F4.getFileNames() == {"A", "B", "C", "Hi"})
 print("Passed!")

testFileFolder()

class Cookie(object):
 def __init__(self, flavor):
  self.flavor, self.toppings = flavor, []
 def addTopping(self, topping):
  self.toppings.append(topping)
 def __repr__(self):
  return f'{self.flavor} cookie with {len(self.toppings)} toppings'
 def __eq__(self, other):
  return isinstance(other, Cookie) and repr(self) == repr(other)
class SmolCookie(Cookie):
 def addTopping(self, topping):
  if len(self.toppings) == 2: self.toppings.pop(0)
  super().addTopping(topping)
def ct1():
 c1 = Cookie('Chocolate')
 c2 = SmolCookie('Chocolate')
 print(c1)
 c1.addTopping('garlic')
 c2.addTopping('cheese')
 print(c1 == c2, c2 == c1)
 for i in range(10):
  c2.addTopping('mayo')
 print(c2.toppings)
ct1()

def ct2(L):
 s = set(L)
 d1 = {}
 d2 = dict()
 for elem in s:
  d1[elem] = L.count(elem)
 print(d1)
 for key in d1:
  if d1[key] in s:
   val = d1[key]
   d2[val] = d2.get(val, set())
   d2[val].add(key)
 return d2
print(ct2([1,1,1,2,4,4,5]))


def ct3(L, s=1, depth=1):
 if L == []:
  result = 0
 elif len(L) == 1:
  result = L[0] * s
 else:
  mid = len(L) // 2
  if mid % 2 == 0:
   newS = s
  else:
   newS = -s
   a = ct3(L[:mid], s, depth+1)
   b = ct3(L[mid:], newS, depth+1)
   result = a + b
 print('*' * depth, result)
 return result
L = [15, 112, 10]
print(ct3(L))
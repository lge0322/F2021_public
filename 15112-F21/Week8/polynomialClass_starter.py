class Polynomial(object):
    def __init__(self, coeffs):  # Complete this method...
        self.coeffs = coeffs[::-1]

    def evalAt(self, x):
        result = 0
        for i in range(len(self.coeffs)):
            curCoeff = self.coeffs[i]
            result += curCoeff * (x ** i)
        return result
       
    def getCoefficient(self, n):
        if n < len(self.coeffs):
            return self.coeffs[n]
        else:
            return 0
        
    def times(self, n):
        newCoeffs = []
        for i in range(len(self.coeffs)):
            newCoeffs.append(self.coeffs[i] * n)
        return Polynomial(newCoeffs[::-1]) #call the new class by referring to class

    def add(self, other):
        xLen = len(self.coeffs)
        yLen = len(other.coeffs)
        newCoeffs = []
        for i in range(max(xLen, yLen)):
            x = self.getCoefficient(i)
            y = other.getCoefficient(i)
            newCoeffs.append(x + y)
        return Polynomial(newCoeffs)

    def __repr__(self):
        value = []
        for power in range(len(self.coeffs)):
            coeff = str(self.coeffs[power]) #we want string values ins of int
            curTerm = ''
            if power == 0:
                curTerm = coeff
            elif power == 1:
                curTerm = coeff + 'x'
            else:
                curTerm = coeff + 'x^' + str(power)
            value.append(curTerm)
        result = value[::-1]
        return " + ".join(result)
        
    def __eq__(self, other):
        return self.coeffs == other.coeffs

    # ...and finish writing the rest of the class

def testPolynomialClass():
    print('Testing Polynomial class...', end='')
    f = Polynomial([2,3,1]) # 2x**2 + 3x + 1, 1,3,2
    assert(f.evalAt(4) == 2*4**2 + 3*4 + 1) # returns f(4), which is 45
    assert(f.evalAt(5) == 2*5**2 + 3*5 + 1) # returns f(5), which is 66
    assert(f.getCoefficient(0) == 1) # get the x**0 coefficient
    assert(f.getCoefficient(1) == 3) # get the x**1 coefficient
    assert(f.getCoefficient(2) == 2) # get the x**2 coefficient
    assert(f.getCoefficient(33) == 0) # assume leading 0's...
    g = f.times(10) # g is a new polynomial, which is 10*f
                    # just multiply each coefficient in f by this value
                    # so g = 20x**2 + 30*x + 10
    assert(g.getCoefficient(0) == 10) # get the x**0 coefficient
   # assert(g.getCoefficient(1) == 30) # get the x**1 coefficient
   
   # assert(g.getCoefficient(2) == 20) # get the x**2 coefficient
   # assert(g.getCoefficient(33) == 0) # assume leading 0's...
    #assert(g.evalAt(4) == 20*4**2 + 30*4 + 10) # returns g(4), which is 450

    #m = f.add(f, g) # m is a new polynomial, which is f + g
    #assert(m.getCoefficient(0) == 11) # get the x**0 coefficient
    #assert(m.getCoefficient(1) == 33) # get the x**1 coefficient
    #assert(m.getCoefficient(2) == 22) # get the x**2 coefficient
    #assert(m.getCoefficient(33) == 0) # assume leading 0's...

    # The printing representation should be as follows:
    assert(str(f) == "2x^2 + 3x + 1")
    assert(str(g) == "20x^2 + 30x + 10")

    # There should also be a way to compare instances
    assert(f == f.times(1))

    print('Passed!')

testPolynomialClass()

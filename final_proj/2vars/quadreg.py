def sigmax(x,y):
     return sum(x)
def sigmay(x,y):
    return sum(y)
def sigmaxsq(x,y):
    a = []
    for i in x:
        a.append(i ** 2)
    return sum(a)
def sigmaysq(x,y):
    a = []
    for i in y:
        a.append(i ** 2)
    return sum(a)
def sigmaxy(x,y):
    a = []
    for i in range(len(x)):
        b = x[i] * y[i]
        a.append(b)
    return sum(a)
def amt(x,y):
    return len(x)
def sigmaxcube(x,y):
    a = []
    for i in x:
        a.append(i ** 3)
    return sum(a)
def sigmaxfour(x,y):
    a = []
    for i in range(len(x)):
        a.append(x[i] ** 4)
    return sum(a)
def sigmaxtwoy(x,y):
    a = []
    for i in range(len(x)):
        b = x[i] ** 2
        c = b * y[i]
        a.append(c)
    return sum(a)
def sigmaxx(x,y):
    a = sigmaxsq(x,y)
    b = sigmax(x,y) ** 2
    c = b / float(amt(x,y))
    return a - c
def sigmaxyb(x,y):
    a = sigmaxy(x,y)
    b = sigmax(x,y) * sigmay(x,y)
    c = b / float(amt(x,y))
    d = a - c
    return d
def sigmaxx2(x,y):
    a = sigmaxcube(x,y)
    b = sigmaxsq(x,y) * sigmax(x,y)
    c = b / float(amt(x,y))
    d = a - c
    return d
def sigmax2y(x,y):
    a = sigmaxtwoy(x,y)
    b = sigmaxsq(x,y) * sigmay(x,y)
    c = b / float(amt(x,y))
    d = a - c
    return d
def sigmax2x2(x,y):
    a = sigmaxfour(x,y)
    b = sigmaxsq(x,y)
    c = b ** 2
    d = c / float(len(x))
    return a - d

def togeta(x,y):
     a = sigmax2y(x,y)
     b = sigmaxx(x,y)
     c = a * b
     d = sigmaxyb(x,y)
     e = sigmaxx2(x,y)
     f = d * e
     g = c - f
     h = b * sigmax2x2(x,y)
     i = h - e ** 2
     return g / float(i)
def togetb(x,y):
     a = sigmaxyb(x,y)
     b = sigmax2x2(x,y)
     c = a * b
     d = sigmax2y(x,y)
     e = sigmaxx2(x,y)
     f = d * e
     g = c - f
     h = sigmaxx(x,y)
     i = b * h
     j = i - (e ** 2)
     return g / float(j)
def togetc(x,y):
     a = sigmay(x,y)
     b = float(len(y))
     c = a / b
     d = sigmax(x,y)
     e = togetb(x,y)
     f = (d / b) * e
     g = c - f
     h = togeta(x,y)
     i = sigmaxsq(x,y)
     j = i / b
     k = j * h
     l = g - k
     return l
def togetcoeffcor1(x,y):
     a = sigmaxy(x,y)
     b = float(len(x))
     c = sigmax(x,y)
     d = sigmay(x,y)
     e = float(c * d)
     f = (a * b) - e
     g = sigmaxsq(x,y)
     h = g * b
     i = h - (c ** 2)
     j = sigmaysq(x,y) * b
     k = d ** 2
     l = j - k
     m = l * i
     n =  m ** .5
     return (f / n) ** 2
# RUN THE FUNCTION BELOW FOR THE ANSWER
def togetitall(x,y):
     print "The quadratic that best fits your data is: y = " + str(togeta(x,y)) + "x^2 + " + str(togetb(x,y)) + "x + " + str(togetc(x,y))
     print "The R^2 value produced was: " + str(togetcoeffcor1(x,y))
     print "While this R^2 value is not correct, it follows the only formulas I found online."
     
     

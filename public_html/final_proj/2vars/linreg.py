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
def togeta(x,y):
    h = sigmay(x,y)
    i = sigmaxsq(x,y)
    j = h * i
    k = sigmax(x,y)
    l = sigmaxy(x,y)
    m = k * l
    n = j - m
    o = i * amt(x)
    p = k ** 2
    q = o - p
    return n / float(q)
def togetb(x,y):
    a = sigmaxy(x,y)
    b = a * amt(x)
    c = sigmax(x,y) * sigmay(x,y)
    d = b - c
    e = sigmaxsq(x,y) * amt(x)
    f = sigmax(x,y) ** 2
    g = e - f
    return d / float(g)
def sigma(x):
    return sum(x)
def amt(x):
    return len(x)
def mean(x):
    a = sigma(x)
    b = float(amt(x))
    c = a / b
    return c
def variancepopulation(x):
    a = mean(x)
    b = 0
    for i in x:
        c = i - a
        b += c ** 2
    d = b / float(amt(x))
    return d
def standarddeviationpopulation(x):
    a = variancepopulation(x)
    return a ** .5

def corrcoeffxy(x,y):
    a = []
    b = mean(x)
    c = mean(y)
    d = standarddeviationpopulation(x)
    e = standarddeviationpopulation(y)
    for i in range(len(x)):
        f = (x[i] - b) / float(d)
        g = (y[i] - c) / float(e)
        a.append(f*g)
    h = sum(a)
    return h / float(amt(x))

def togetmxplusb(x,y):
    print "y = " + str(togeta(x,y)) + "x + " + str(togetb(x,y))
    print "The Correlation Coefficient is: " + str(corrcoeffxy(x,y))

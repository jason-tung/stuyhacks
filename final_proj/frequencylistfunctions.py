import math

def frequencylistgenerator(x,y):
    a = []
    for i in range(len(x)):
        for z in range(y[i]):
            a.append(x[i])
    return a

def sigmafrequencylist(x,y):
    x = frequencylistgenerator(x,y)
    return sum(x)

def amtfrequencylist(x,y):
    x = frequencylistgenerator(x,y)
    return len(x)

def meanfrequencylist(x,y):
    a = sigmafrequencylist(x,y)
    b = float(amtfrequencylist(x,y))
    c = a / b
    return c

def medianfrequencylist(x,y):
    g = frequencylistgenerator(x,y)
    g.sort()
    a = len(g)
    if a % 2 != 0:
        b = (a-1)/2
        return g[b]
    else:
        b = (a-1)/2.
        c = int(math.ceil(b))
        d = int(math.floor(b))
        return (g[c] + g[d])/2.

def median(x):
    x.sort()
    a = len(x)
    if a % 2 != 0:
        b = (a-1)/2
        return x[b]
    else:
        b = (a-1)/2.
        c = int(math.ceil(b))
        d = int(math.floor(b))
        return (x[c] + x[d])/2.

def q1q3frequencylist(y,z):
    x = frequencylistgenerator(y,z)
    x.sort()
    b = median(x)
    c = len(x)
    if c % 2 != 0:
        d = x.index(b)
        e = x[:d]
        f = x[d + 1:]
        g = median(e)
        h = median(f)
        return g,h
    else:
        d = (c-1)/2.
        e = int(math.ceil(d))
        f = int(math.floor(d))
        g = x[:f]
        h = x[e + 1:]
        i = median(g)
        j = median(h)
        return i, j
    
def interquartilerange(x,y):
    a,b = q1q3(x,y)
    return b - a

def modefrequencylist(x,y):
    a = y.index(max(y))
    if y.count(max(y)) > 1:
        return "No Mode"
    else:
        return x[a]

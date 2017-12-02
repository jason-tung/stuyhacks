import math

def sigma(x):
    return sum(x)

def amt(x):
    return len(x)

def mean(x):
    a = sigma(x)
    b = float(amt(x))
    c = a / b
    return c

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

def q1q3(x):
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

def interquartilerange(x):
    a,b = q1q3(x)
    return b - a

def outlierfinder(x):
    a,b = q1q3(x)
    c = interquartilerange(x)
    d = a - (1.5 * c)
    e = b + (1.5 * c)
    f = []
    for i in x:
        if i < d or i > e:
            f.append(i)
    if len(f) == 0:
        return "No Outliers"
    else:
        return f

def range(x):
    x.sort()
    return x[-1] - x[0]

def most(x):
    a = {}
    for i in x:
        if i in a:
            a[i] = a[i] + 1
        else:
            a[i] = 1
    return a

def mode(x):
    d = most(x)
    l = []
    for key in d.keys():
        if d[key] == max(d.values()):
            l.append(key)
    if len(l) > 1:
        return "No Mode"
    else:
        return l[0]

def variancepopulation(x):
    a = mean(x)
    b = 0
    for i in x:
        c = i - a
        b += c ** 2
    d = b / float(amt(x))
    return d

def variancesample(x):
    a = mean(x)
    b = 0
    for i in x:
        c = i - a
        b += c ** 2
    d = b / float(amt(x) - 1)
    return d

def standarddeviationpopulation(x):
    a = variancepopulation(x)
    return a ** .5

def standarddeviationsample(x):
    a = variancesample(x)
    return a ** .5



    

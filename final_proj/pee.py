#! /usr/bin/python
import math
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
     if n  == 0:
          return "Error!"
     else:
          return (f / n) ** 2
# RUN THE FUNCTION BELOW FOR THE ANSWER
def togetitall(x,y):
     print "The quadratic that best fits your data is: y = " + str(togeta(x,y)) + "x^2 + " + str(togetb(x,y)) + "x + " + str(togetc(x,y))
     print "<br>The R^2 value produced was: " + str(togetcoeffcor1(x,y))
     
     

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
    if d == 0 or e == 0:
        a = togeta(x,y)
        if a >= 0:
            return str(1)
        else:
            return str(-1)
    else:
        for i in range(len(x)):
            f = (x[i] - b) / float(d)
            g = (y[i] - c) / float(e)
            a.append(f*g)
        h = sum(a)
        return h / float(amt(x))

def togetmxplusb(x,y):
    print "y = " + str(togetb(x,y)) + "x + " + str(togeta(x,y))
    print "<br>The Correlation Coefficient is: " + str(corrcoeffxy(x,y))
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
    if len(x) > 4:
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
    else:
        return "The Sample is too Small!"

def interquartilerange(x):
    if len(x) > 4:
        a,b = q1q3(x)
        return b - a
    else:
        return "The Sample is too small!"

def outlierfinder(x):
    if len(x) > 4:
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
        return "The Sample is too small!"

def rangee(x):
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

def onevars():
    o = frequency()
    print "mean:",mean(o)
    print "<br>"
    print "maximum:",max(o)
    print "<br>"
    print "minimum:",min(o)
    print "<br>"
    print "(q1,q3):",q1q3(o)
    print "<br>"
    print "median:",mean(o)
    print "<br>"
    print "sigma(x)",sigma(o)
    print "<br>"
    print "range:",rangee(o)
    print "<br>"
    print "mode:",mode(o)
    print "<br>"
    print "interquartile range:",interquartilerange(o)
    print "<br>"
    print "outliers:",outlierfinder(o)
    print "<br>"
    print "population variance:",variancepopulation(o)
    print "<br>"
    print "sample variance:",variancesample(o)
    print "<br>"
    print "population standard deviation:",standarddeviationpopulation(o)
    print "<br>"
    print "sample standard deviation:",standarddeviationsample(o)



def twovars():
    t = regular()
    x = t[0]
    y = t[1]
    print "sigmax sq:",sigmaxsq(x,y)
    print "<br>"
    print "sigmay sq:",sigmaysq(x,y)
    print "<br>"
    print 'sigmax:',sigmax(x,y)
    print "<br>"
    print 'sigmay:',sigmay(x,y)
    print "<br>"
    print 'population size:',amt(x)
    print "<br>"
    print "LINEAR REGRESSION:<BR>"
    togetmxplusb(x,y)
    print "<BR>"
    print "QUADRATIC REGRESSION:<BR>"
    togetitall(x,y)


HTML_Header='Content-type: text/html\n\n'

head = """<doctype! html>
<html>
<head>
<title> i wasted 12 hours of my life </title>
<link rel="icon" type="image/png" href="https://image.flaticon.com/icons/png/128/25/25305.png" />
<link rel="stylesheet" type="text/css" href="csshake.min.css">
<link rel="stylesheet" type="text/css" href="http://csshake.surge.sh/csshake.min.css">
<link rel="stylesheet" href="css/bootstrap.min.css">
<link rel="stylesheet" href="font.css">
<link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet">
<style>
body{
font-family:poppins;
color: #ffffff;
font-size:20px;
	background-image:url(poo);
	background-size:100% 100%;
	background-repeat:no-repeat;
	background-position: center;
}
th,button,input,text{
font-family:poppins
}
td,th{
text-align:center;
}
div{
padding:10px;
background: rgba(0,0,0,0.5);
width: 70%
position:fixed;
top 50%
}

</style>
</head>
"""


import cgi, cgitb
cgitb.enable()

def flist():
    form = cgi.FieldStorage()
    isfreq = form.getvalue('freq','False')
    return isfreq == 'True'

def regular():
    form = cgi.FieldStorage()
    num = form.getvalue('num','nonum')
    try:
        num = int(num)
    except:
        return 'rowerror'
    l1=[]
    l2=[]
    
    for index in range(num):
        index += 1
        strindex = str(index)
        if index <= 9:
            strindex = "0"+strindex
        f1 = form.getvalue('L1-%s'%strindex,'missingx')
        f2 = form.getvalue('L2-%s'%strindex,'missingy')
        try:
            f1=float(f1)
            f2=float(f2)
        except:
            return 'listerror'
        l1.append(f1)
        l2.append(f2)
    return [l1,l2]

def orderedpairs():
    masterlist = regular()
    l = []
    length = len(masterlist[0])
    for poop in range(length):
        l.append((masterlist[0][poop],masterlist[1][poop]))
    return l
				
def frequency():
    newl = []
    masterlist = regular()
    length = len(masterlist[0])
    for index in range(length):
        try:
            f = int(masterlist[1][index])
        except:
            return "freqerror"
        for frequencies in range(f):
            newl.append(masterlist[0][index])
    return newl
						
print HTML_Header
print head
print "<body><center><br><br><div>"
if flist():
    if type(frequency()) != list:
        print "check your inputs and the form at the top"
    else:
        print "Here is the frequency list you input in a list format:<br>"
        print frequency(),"<br>"
        onevars()
else:
    if type(regular()) != list:
        print 'check your inputs and the form at the top'
    else:
        print "Here is the list you input in an ordered pair format:<br>"
        print orderedpairs(),"<br>"
        twovars()
print "</div></center></body></html>"


    















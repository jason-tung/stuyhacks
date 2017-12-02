#! /usr/bin/python
# -*- coding: utf-8 -*-
import cgi, cgitb,urllib2,sys
cgitb.enable()

first=  "Content-type: text/html\n\n"

nextt = """<doctype! html>
<html>
<head>
<link rel="icon" type="image/png" href="https://image.flaticon.com/icons/png/128/25/25305.png" />
<link rel="stylesheet" type="text/css" href="csshake.min.css">
<link rel="stylesheet" type="text/css" href="http://csshake.surge.sh/csshake.min.css">
<link rel="stylesheet" href="css/bootstrap.min.css">
<link rel="stylesheet" href="font.css">
<link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet">
<style>
th,button,input,text{
font-family:poppins
}
td,th{
text-align:center;
}
div{
padding:10px;
}
</style>
</head>
<body>
<form>
<center>
<div>
<input type = "submit" name = "the_button" value = "submit you idiot">
</div>
<br>
<table border= "1" width = '50%'><form method = "get" action = "pee.py">
<tr>
	<th>L1</th>
	<th>L2</th>
</tr>
"""

fin = """
</table>
</center>
</form>
</body>
</html>
"""
form = cgi.FieldStorage()
howmany = form.getvalue("japanesebullettrain","**no**")
try:
    howmany = int(howmany)
except:
    print "give me an integer you clown"
if type(howmany) == int:
    for index in range(howmany):
        index += 1
        i = index
        index = str(index)
        if i < 10:
            index = "0"+index
        m = ''
        m+='<tr>'
        m+='<td>'
        m+='''%s <input type = "text" name = "L1-%s">''' % ("L1-"+index,index)
        m+='</td>'
        m+='<td>'
        m+='''%s <input type = "text" name = "L2-%s">''' % ("L2-"+index,index)
        m+='</td>'
        m+='</tr>'

    print first
    print nextt
    print m
    print fin










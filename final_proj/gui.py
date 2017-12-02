#! /usr/bin/python
# -*- coding: utf-8 -*-
import cgi, cgitb,urllib2,sys
cgitb.enable()

first=  "Content-type: text/html\n\n"

head = """<doctype! html>
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
color:rgb(191, 191, 191)
}
td,th{
text-align:center;
}
td,th{
color:rgb(191, 191, 191)
}
div{
padding:10px;
background: rgba(0,0,0,0.5);
width: 50%
}
body{
	background-image:url(poo.gif);
	background-color:white;
	background-size:100% 100%;
	background-repeat:no-repeat;
	background-position: center;
	font-family:poppins; 
	color: rgb(191, 191, 191)
}
.table1 {
background: rgba(0,0,0,0.5);
}

</style>
</head>
"""
body ="""
<body>
<form method = "get" action = "pee.py">
<center>
<div>
i'm bad at coding so if you want 1-var stats you need to turn on frequency and enter 1 for the frequency<br>
if you're looking for regressions, please don't enter non functions :/
<br>
<input type = "submit" name = "fa" value = "submit you idiot" style = "color:rgba(0,0,0,0.5)"><br>
Is this a frequency list? <input type = "checkbox" name = "freq" value = "True"><br>
how many lines did you use <input type = "text" name = "num" size = "3">
</div>
<br>
<table border= "1" width = '50%' class = 'table1' style = "padding:20px;"><form method = "get" action = "pee.py">
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
def main():
    form = cgi.FieldStorage()
    howmany = form.getvalue("num","f")
    try:
        howmany = int(howmany)
    except:
        pass
    if type(howmany) == int and howmany>=1:
        m = ''
        for index in range(howmany):
            index += 1
            i = index
            index = str(index)
            if i < 10:
                index = "0"+index
            m+='<tr>'
            m+='<td>'
            m+='''%s <input type = "text" name = "L1-%s">''' % ("L1-"+index,index)
            m+='</td>\n'
            m+='<td>'
            m+='''%s <input type = "text" name = "L2-%s">''' % ("L2-"+index,index)
            m+='</td>\n'
            m+='</tr>'
        print first
        print head
        print body
        print m
        print fin
    else:
        print first
        print head
        print '<body><center><div>'
        print "<p style = 'font-size:100px;color:#A2A2A2;padding:50px'>give me a positive integer you clown</p>"
        print '</div></center></body>'
        print "</html>"
main()









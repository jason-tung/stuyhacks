#! /usr/bin/python

import cgi, cgitb
cgitb.enable()


quick_header = "Content-type: text/html\n\n"

def main():
	form = cgi.FieldStorage()
	her_name = form.getvalue("fnork", '')
	superior = form.getvalue("super", "")
	print quick_header
	print "<html><body>"
	print "<title>I see</title>"
	print "You're " + her_name + "?"
	print "</body></html>"
main()


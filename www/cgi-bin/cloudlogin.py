#!/usr/bin/python

import cgi
import cgitb
import time
import commands

cgitb.enable()


print "Content-type:text/html"
print ""
#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()


# taking user name
user=web.getvalue('u')
# taking password 
password=web.getvalue('p')
#for sign up
signup=web.getvalue('sup')

if  user  ==   'root' and password ==  '123' :
	print "<a href='http://192.168.43.228/project.html'>"
	print "Click here to GO Cloud SErvices"
	print "</a>"


else :
	print "The Username or password that you've entered is incorrect"
	time.sleep(2)
	print "<a href='http://192.168.43.228/cloudlogin.html'>"
	print "Click here to try again"
	print "</a>"


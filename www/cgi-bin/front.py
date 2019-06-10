#!/usr/bin/python

import cgi
import cgitb
import commands

cgitb.enable()


print "Content-type:text/html"
print ""
#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()


# taking user_input name
p=web.getvalue('v')


if  p  ==  'hadoop':
	print "<a href='http://192.168.43.228/test1.html'>"
	print "Click here to GO Hadoop login page"
	print "</a>"


else:
	print "<a href='http://192.168.43.228/login.html'>"
	print "Click here to Go Cloud login page"
	print "</a>"




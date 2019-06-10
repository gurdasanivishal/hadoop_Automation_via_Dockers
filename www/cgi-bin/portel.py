#!/usr/bin/python

import cgi
import cgitb
import commands
import os

cgitb.enable()


print "Content-type:text/html"
print ""
#  taking date from apache and storing into web variable hp
web=cgi.FieldStorage()


# taking user_input name
portal=web.getvalue('next')


if  portal  ==  'hp':
	print "<a href='http://192.168.43.228:50070'>"
	print "Click here to GO Hadoop portal"
	print "</a>"


else:
	print 'shutting down all_containers.......'
	print commands.getoutput('sudo docker kill $(docker ps -qa)')




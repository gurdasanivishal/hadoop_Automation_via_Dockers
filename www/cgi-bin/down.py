#!/usr/bin/python

import  cgi
import  commands
import  os

print "Content-type:text/html"
print ""

#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

# only want to access data in x 
store=web.getvalue('shutdown')

#  running commands
if  store == 'dwn':
	print  "<pre>"
	print  commands.getoutput('sudo docker ps')
	print  commands.getoutput('sudo dockerkill')
	print  "</pre>"
	#time.sleep(10)
 	#to go LOGIN portel
	print "<a href='http://192.168.43.228/test1.html'>"
	print "Click here to GO login page"	
	print "</a>"
	print  "</pre>"


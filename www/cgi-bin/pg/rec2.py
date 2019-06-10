#!/usr/bin/python

import  cgi
import  commands

print "Content-type:text/html"
print ""

#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

# only want to access data in x 
store=web.getvalue('c')
#  running commands
if  store ==  'dt' :
	print  "<pre>"
	print  commands.getoutput('date')
	print  "</pre>"

elif  store ==  'iftp' :
	print  "<pre>"
	print  commands.getoutput('sudo yum  install ftp -y')
	print  "</pre>"

elif  store ==  'op' :
	print  commands.getoutput('sudo ifconfig')
	print  "</pre>"
	




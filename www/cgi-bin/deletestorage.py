#!/usr/bin/python2
import commands,os,cgi,time,cgitb
print "Content-type:text/html\n"
print ""
web=cgi.FieldStorage()
deletedrive=web.getvalue('lvname')
buttonname=web.getvalue('button')
commands.getoutput('sudo lvchange -an cloud/'+deletedrive)
commands.getoutput('sudo lvremove  cloud/'+deletedrive)

#commands.getoutput('Do you really want to remove active logical volume roy? [y/n]:y')
commands.getoutput('sudo rmdir /var/www/html/'+deletedrive)
print "Sucessfully Deleted"


#!/usr/bin/python2
import os,sys,time
import commands,os
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#Data is retrieved
data=cgi.FieldStorage()
choice=data.getvalue('radio')

print "run the downloaded .sh file on your terminal"
print "\n"
print "eg:- bash xxx.sh"

if  choice == "Gnome-calculator":

	print "ssh -X 192.168.43.228 gnome-calculator"
	
	
elif  choice == "Vlc":

	print "ssh -X 192.168.43.228 vlc"	

elif  choice == "Gedit":

	print "ssh -X 192.168.43.228 gedit"

else 

	print "ssh -X 192.168.43.228 cheese"

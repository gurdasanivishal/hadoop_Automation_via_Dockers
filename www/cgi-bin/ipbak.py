#!/usr/bin/python

import commands
import os
import time
import cgi,cgitb
cgitb.enable()

print "Content-type:text/html"
print ""

#taking date from apache and storing into web variable 
#web=cgi.FieldStorage()


#for hadoop version 
#h_version=web.getvalue('hv')
#to get cluster size 
#size=web.getvalue('nm')
#for map reduce
#m_reduce=web.getvalue('m')
#to shutdown all containers
#shut_down=web.getvalue('sd')

cont=[]
ip=[]

size=raw_input("Enter cluster size")
#defining list for container
#h_version=raw_input("Enter hadoop version")


for i in range(int(size)):
	cont_id=commands.getoutput("sudo docker run -itd centos6:hadoopv1")
	cont.append(cont_id)

print cont

#getting ip address
for i in cont:
	ips=commands.getoutput('sudo docker exec '+i+' hostname -i')
	ip.append(ips)
	
	
print ip


for i in range(int(size)):
	print commands.getoutput('echo '+ip[i]+'  '+cont[i]+'')

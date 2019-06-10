#!/usr/bin/python2
import commands,os,time,cgi
print "Content-type:text/html\n"
print ""
#taking data from apache and storing into web variable
web=cgi.FieldStorage()
#diskname
disk_name=web.getvalue('diskname')
#name of logical volume
logicalvolume_name=web.getvalue('logicalvolumename')
#size of logical volume
disk_size=web.getvalue('disksize')


#creating physical group
commands.getoutput('sudo pvcreate '+disk_name)
#creating volume group
commands.getoutput('sudo vgcreate  cloud '+disk_name)
#creating logical volume and give size


#commands.getoutput('sudo lvcreate --size '+disk_size+'M --thin cloudst/POOL')
#else :
commands.getoutput('sudo lvcreate --size '+disk_size+'M --thin cloud/'+logicalvolume_name)

#print "hello"


#!/usr/bin/python2
import cgi
import os
import cgitb
import commands
import sys

cgitb.enable()
print "Content-type:text/html"

print ""

#taking data from apache server
data=cgi.FieldStorage()

# os Taking name as input
os_name=data.getvalue('osname')

#Taking os cpu as input
os_cpu=data.getvalue('oscpu')

#Taking os ram as input
os_ram=data.getvalue('osram')

#Taking port number as input
port_no=data.getvalue('portno')


print "done successfully"

if os_name=="rhel7":
	#Creating a snapshot of the pre-installed os
	commands.getstatusoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(os_name))
	
	#Installing the virtual os on the virtual manager
	commands.getstatusoutput('sudo virt-install --name {} --ram {} --vcpu {} --disk path=/var/lib/libvirt/images/{}.qcow2 --import --graphics vnc,listen=192.168.122.1,port=5989 --noautoconsole '.format(os_name,os_ram,os_cpu,os_name))
	
elif os_name =="kali":
	#Creating a snapshot of the os
	commands.getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.43.228,port=5989 --cdrom /root/Downloads/kali-linux-2.0-amd64.iso --ram {} --vcpu {}  --nodisk --name {} --noautoconsole '.format(os_ram,os_cpu,os_name))

else :
       #Creating a snapshot of the os
       commands.getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.43.228,port=5989 --cdrom /root/Downloads/ubuntu-16.04.3-desktop-amd64.iso --ram {} --vcpu {}  --nodisk --name {} --noautoconsole '.format(os_ram,os_cpu,os_name))
	




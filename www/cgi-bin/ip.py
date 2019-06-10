#!/usr/bin/python

import commands,os
import time
import cgi,cgitb
cgitb.enable()

print "Content-type:text/html"

print ""

size=int(raw_input('enter cluster size'))
#web=cgi.FieldStorage()

#to get cluster size 
#size=web.getvalue('nm')

#m_reduce=web.getvalue('m')
print size

cont=[]
ip=[]

for i in range(int(size)):
	cont_id=commands.getoutput("sudo docker run -itd  centos6:hadoop2new")
	cont.append(cont_id)

#print cont
#print cont

#getting ip address
for i in cont:
	ips=commands.getoutput('sudo docker exec '+i+' hostname -i')
	ip.append(ips)
	
	
print ip
for i in range(int(size)):
	f=open('a.txt','a')
	f.write("" +ip[i]+ "    " +cont[i]+ ""+'\n')
	f.close()
'''
print commands.getoutput('sudo docker exec -u 0 '+cont[0]+' -c print("'+ip[0]+'   '+cont[0]+'") >>/etc/hosts')

#print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/namenode/core-site.xml  '+cont[0]+':/hadoop2/etc/hadoop/')
print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/namenode/hdfs-site.xml  '+cont[0]+':/hadoop2/etc/hadoop/')
#print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/resourcemanager/mapred-site.xml  '+cont[0]+':/hadoop2/etc/hadoop/')   
#print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/resourcemanager/yarn-site.xml  '+cont[0]+':/hadoop2/etc/hadoop/')   
print commands.getoutput('sudo docker exec '+cont[0]+' /hadoop2/bin/hdfs namenode -format')
print commands.getoutput('sudo docker exec '+cont[0]+' /hadoop2/sbin/hadoop-daemon.sh start namenode')
if m_reduce == 'mp': 
	print commands.getoutput('sudo docker exec '+cont[0]+' /hadoop2/sbin/yarn-daemon.sh start resourcemanager')


for i in range(1,int(size)):
	
	#print commands.getoutput('sudo docker cp --privileged /root/Desktop/hack/hosts2  '+cont[i]+' :/etc/')
	print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/datanode/hdfs-site.xml '+cont[i]+':/hadoop2/etc/hadoop/')
	print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/datanode/core-site.xml  '+cont[i]+':/hadoop2/etc/hadoop/')
	print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/tasktracker/yarn-site.xml '+cont[i]+':/hadoop2/etc/hadoop/')   
	print commands.getoutput('sudo docker exec '+cont[i]+'  /hadoop2/sbin/hadoop-daemon.sh start datanode')
	if m_reduce == 'mp':	
		print commands.getoutput('sudo docker exec '+cont[i]+' /hadoop2/sbin/yarn-daemon.sh start nodemanager')

print "<a href='http://192.168.43.228/portal.html'>"	
print "Click here to GO next page"
print "</a>"
'''

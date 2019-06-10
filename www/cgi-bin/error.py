#!/usr/bin/python

import commands
import time
import cgi,cgitb
cgitb.enable()

print "Content-type:text/html"

print ""


web=cgi.FieldStorage()

#to get cluster size 
size=web.getvalue('nm')
m_reduce=web.getvalue('m')
print size


cont=[]
ip=[]

for i in range(int(size)):
	cont_id=commands.getoutput("sudo docker run -itd centos6:hadoopv11")
	cont.append(cont_id)

print cont

#getting ip address
for i in cont:
	ips=commands.getoutput('sudo docker exec '+i+' hostname -i')
	ip.append(ips)
	
	
print ip


print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop1/namenode/hdfs-site.xml '+cont[0]+' :/etc/hadoop/')
print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop1/jobtracker/mapred-site.xml '+cont[0]+' :/etc/hadoop/')   
print commands.getoutput('sudo docker exec '+cont[0]+' iptables -F')
print commands.getoutput('sudo docker exec '+cont[0]+' setenforce 0')			
print commands.getoutput('sudo docker exec '+cont[0]+' hadoop namenode -format')
print commands.getoutput('sudo docker exec '+cont[0]+' hadoop-daemon.sh start namenode')
if m_reduce == 'mp': 
	print commands.getoutput('sudo docker exec '+cont[0]+' hadoop-daemon.sh start jobtracker')


for i in range(1,int(size)):
	
	print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop1/datanode/hdfs-site.xml '+cont[i]+' :/etc/hadoop/')
	print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop1/tasktracker/mapred-site.xml '+cont[i]+' :/etc/hadoop/')   
	print commands.getoutput('sudo docker exec '+cont[i]+' iptables -F')
	print commands.getoutput('sudo docker exec '+cont[i]+' setenforce 0')			
	print commands.getoutput('sudo docker exec '+cont[i]+' hadoop-daemon.sh start datanode')
	if m_reduce == 'mp':	
		print commands.getoutput('sudo docker exec '+cont[i]+' hadoop-daemon.sh start tasktracker')
print "@@@@@@ please wait @@@@@@@"
print "<a href='http://192.168.43.228/portal.html'>"	
print "Click here to GO next page"
print "</a>"

#!/usr/bin/python

import commands
import cgi,cgitb;
cgitb.enable()

print "Content-type:text/html"

print ""

#taking date from apache and storing into web variable 
web=cgi.FieldStorage()

 
#to get cluster size 
size=web.getvalue('nm')
#for map reduce
m_reduce=web.getvalue('m')

print size

cont=[]
ip=[]

for i in range(int(size)):
	cont_id=commands.getoutput("sudo docker run -itd centos6:hadoop2new")
	cont.append(cont_id)

print cont

#getting ip address
for i in cont:
	ips=commands.getoutput('sudo docker exec '+i+' hostname -i')
	ip.append(ips)
	

print ip

print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/namenode/hdfs-site.xml '+cont[0]+' :/hadoop2/etc/hadoop/')
#print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/namenode/hadoop-evm.sh '+cont[0]+' :/hadoop2/etc/hadoop/')
print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/resourcemanager/mapred-site.xml '+cont[0]+' :/hadoop2/etc/hadoop/')
print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/resourcemanager/yarn-site.xml '+cont[0]+' :/hadoop2/etc/hadoop/')   
#print commands.getoutput('sudo docker exec '+cont[0]+' iptables -F')
print commands.getoutput('sudo docker exec '+cont[0]+' setenforce 0')			
print commands.getoutput('sudo docker exec '+cont[0]+' hdfs namenode -format')
print commands.getoutput('sudo docker exec '+cont[0]+' hadoop-daemon.sh start namenode')
if m_reduce=='mp':
	print commands.getoutput('sudo docker exec '+cont[0]+' yarn-daemon.sh start resourcemanager')


for i in range(1,int(size)):
	
	print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/datanode/hdfs-site.xml '+cont[i]+' :/hadoop2/etc/hadoop/')
	#print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/datanode/hadoop-evm.sh '+cont[i]+' :/hadoop2/etc/hadoop/')
	print commands.getoutput('sudo docker cp /root/Desktop/hack/hadoop2/nodemanager/yarn-site.xml '+cont[i]+' :/hadoop2/etc/hadoop/')   
	#print commands.getoutput('sudo docker exec '+cont[i]+' iptables -F')
	print commands.getoutput('sudo docker exec '+cont[i]+' setenforce 0')			
	print commands.getoutput('sudo docker exec '+cont[i]+' hadoop-daemon.sh start datanode')
	if m_reduce=='mp':
		print commands.getoutput('sudo docker exec '+cont[i]+' yarn-daemon.sh start nodemanager')

#to go hadoop portel
#print "<a href='http://192.168.43.228/portal.html'>"	
#print "Click here to GO next page"
#print "</a>"



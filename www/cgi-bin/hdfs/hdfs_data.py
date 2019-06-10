#!/usr/bin/python

import csv
import  commands
import cgi,cgitb
cgitb.enable()

print "Content-type:text/html"

print ""

web=cgi.FieldStorage()

#to get file 
data_file=web.getvalue('file')

commands.getoutput("cat a.txt | awk '{print $2 " "}' >hdfs.txt")
x = []

f=open('hdfs.txt')
for i in f:
	j=i.split()[0]
	x.append(j)
#a=x[2]
#print a
print commands.getoutput('sudo docker exec '+cont[2]+' hadoop fs -put data_file  /data')
f.close()

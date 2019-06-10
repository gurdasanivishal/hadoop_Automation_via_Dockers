#!/usr/bin/python

import cgi
import mysql.connector  as mysql

print "content-type:text/html"
print  ""

web=cgi.FieldStorage()

name=web.getvalue('n')
email=web.getvalue('e')
idd=web.getvalue('sr')

print  name
print  email
print  idd
#  connecting to database 
conn=mysql.connect(user='root',password='redhat',host='localhost',database='adhoc')
cur=conn.cursor()
q="select * from info;"
cur.execute(q)
output=cur.fetchall()
conn.close()
if len(output):
    print "Hello world"
else :
print "no hello world"

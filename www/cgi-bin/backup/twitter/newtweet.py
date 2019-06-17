#!/usr/bin/python
import tweepy,time
import sys,time
import csv
import pandas as pd
from textblob import TextBlob 
import cgi,cgitb
cgitb.enable()

print "Content-type:text/html"

print ""

web=cgi.FieldStorage()

#to get cluster size 
topic=web.getvalue('nm')



#to authenticate twitter from ur account 
consumer_key="<enter your consumer_key >"
consumer_secret= "<enter your consumer_secret >"

#to authenticate
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

#create secret key and access key 
access_key="<enter your access key>"
access_secret="<enter yout access secret>"

#here auth is very much similar to session variable
auth.set_access_token(access_key,access_secret)

#to connect
connected=tweepy.API(auth)

#now finding data
#print(dir(connect))
#       number of tweets
#import sys 
#topic=sys.argv[1]
#print(topic)

csvFile = open('tweet.csv', 'a')
csvWriter = csv.writer(csvFile)

get_data=connected.search(topic,count=10)
#print get_data
f=open('ttt.txt','w')
f.close

for i in get_data:

	analysis=TextBlob(i.text)
	#print(analysis)
	#time.sleep(2)
	print(analysis.sentiment)
	#print (i.created_at, i.text)	
	f=open('ttt.txt','a')
	f.write(str(analysis.sentiment)+'\n')
	#csvWriter.writerow([i.created_at, i.text.encode('utf-8')])
	#csvWriter.writerow(i['analysis.sentiment'])



print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print  "@@@@Please Wait graph is being prepared @@@@@@"
print  "@@@@                                     @@@@@@"
print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

#time.sleep(5)

execfile('graph.py')


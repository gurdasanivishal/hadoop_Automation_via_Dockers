#!/usr/bin/python

import matplotlib.pyplot as plt
import csv
import  commands
# cutting  file pnum
commands.getoutput("cat ttt.txt  |  awk -F'('  '{print $2}'  |  cut -d,  -f1  | cut -d= -f2  >pnum.txt")
commands.getoutput("cat ttt.txt  |  awk -F'('  '{print $2}'  |  cut -d,  -f2  | cut -d= -f2 |  cut -d')' -f1  >snum.txt")

x = []
y = []

f=open('pnum.txt')
for i in f:
	j=i.split()[0]
	x.append(j)

print  x
f.close()


f=open('snum.txt')
for i in f:
	j=i.split()[0]
	y.append(j)

print  y
f.close()
'''
with open('tweet.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

'''
plt.plot(x,y)
plt.plot(y,x)
plt.scatter(x,y, label='polarity/sensitivity',s=100,c='r')
plt.scatter(y,x, label='sensitivity/polarity',s=150,c='g',marker='*')
plt.xlabel('polarity')
plt.ylabel('sensitivity')
plt.title('SEntiment graphs')
plt.legend()
plt.show()

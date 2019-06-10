#!/usr/bin/python2
import  cgi,commands,os,time,cgitb
#import storedata
print "Content-type:text/html\n"
print ""
#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

#  drive name 
drive_name=web.getvalue('dn')
#  drive size in MB 
drive_size=web.getvalue('ds')
#drive_size2=str(drive_size)
button_name=web.getvalue('button')
#f=open("demo.txt", "w+")

#f.write(drive_name)
#f.close()
#  creating  thin LVM  partition 

commands.getoutput('sudo lvcreate  --name  '+drive_name+'  -V'+drive_size+'M   --thin  cloud/pool1')

#  now formating the Partion 
commands.getoutput('sudo mkfs.xfs    /dev/cloud/'+drive_name)

#  mount storage  on server side first  
commands.getoutput('sudo mkdir   /var/www/html/'+drive_name)
# now mounting 
commands.getoutput('sudo mount  /dev/cloud/'+drive_name+'       /var/www/html/'+drive_name)
#os.system('cd /var/www/'+drive_name+'/ ;touch index.txt')
print "<meta http-equiv='refresh' content='1;url=http://192.168.122.44/uploadpage.html'/>"
#commands.getoutput("sudo cp /var/www/html/uploadpage.html  /var/www/html/"+drive_name+"/")

'''
#print commands.getoutput('sudo cd  /ggg/ ;> jdnj2.txt')
#time.sleep(2)
#link = "http://127.0.0.1/"+drive_name
"""
<html>
<body>
<p>Your Storage Is Sucessfully Generated</p>
<a href=http://192.168.122.44/drive_name><button>Go To Storage</button></a>
</body>
</html>
      """

#print "you are done file has created"
#print "<meta http-equiv='refresh' content='5;http://127.0.0.1/"+drive_name+"' >"
#os.system('cd /var/www/html/'+drive_name+'/ ;touch jdnj2.txt')
#commands.getoutput('cd /var/www/'+drive_name+'/'+'touch'+ index.txt)

#execfile('storedata.py')
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
	fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
	open('/var/www/html/'+drive_name+'/'+ fn, 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully'
   
else:
	message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)
'''

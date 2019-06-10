#!/usr/bin/python2

import cgi, os
import cgitb
cgitb.enable()
#import objectstorage 
#from objectstorage import drive_name
form = cgi.FieldStorage()
#print drive_name
#print drive_size2
#x = objectstorage.drive_name
#print(drive_name)

# Get filename here.
fileitem = form['filename']
#drive_name=form.getvalue('dn')
button_name=form.getvalue('button')
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
	fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
	open('/var/www/html/gotohell/'+ fn, 'wb').write(fileitem.file.read())
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


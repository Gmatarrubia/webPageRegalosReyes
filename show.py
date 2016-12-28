#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
# Import modules for sqlite
import sqlite3

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
#Declaracion db y cursor
db = sqlite3.connect('lista.db')
cursor = db.cursor()

# Get data from fields
nombre = form.getvalue('nombre')
code   = form.getvalue('code')
code   = int(code)
key    = ord(nombre[0])+100
cursor.execute("SELECT name from sqlite_master WHERE type='table';")
aux = cursor.fetchall()
lista = []
for i in aux:
        lista.append(i[0])
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Lista de deseos:</title>"
print "</head>"
print "<body>"
#print "<h2>Code: %s Key: %s</h2>" % (code, key)  #only for debugging
if code==key:
    #print "<h2>Son iguales</h2>" #only for debbuging
    print """<form action="/cgi-bin/update.py " method="POST">"""
    for tabla in lista:
	#if tabla != nombre.lower():
		print "<h2> Lista de %s:</h2>" % (tabla)
    		cursor.execute("SELECT * FROM %s" % (tabla.lower()) )
    		ideas = cursor.fetchall()
    		for i in ideas:
			if tabla != nombre.lower():
				print "<input type=\"checkbox\" name=\"%s\" value=1 >" % (i[0])
			print  i[0]
			if tabla != nombre.lower():
				print " - " + i[1]
			print "<br>"
    print "<input type=\"hidden\" name=\"nombre\" value=\"%s\" >" % nombre
    print "<input type=\"hidden\" name=\"code\" value=\"%s\" >" % code
    print """<input type="submit" value="Asignar">"""
    print "</form>"
    db.close()
else:
    print "<h2>Clave incorrecta.</h2>"

print """<form action="http://192.168.1.106" method="POST">
           <input type="submit" value="Volver">
         </form>"""

print "</body>"
print "</html>"

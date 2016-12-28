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
#####print form ##### only for debugging
for tabla in lista:
	if tabla != nombre.lower():
		cursor.execute("SELECT * FROM %s" % (tabla.lower()) )
		ideas = cursor.fetchall()
		for i in ideas:
			if i[0] in form:
				cursor.execute("UPDATE \"%s\" set asignado=\"%s\" where idea=\"%s\" " % (tabla, nombre.lower(), i[0]))
db.commit()
db.close()
print "<h2> Asignado correcto </h2>"

print """<form action="/cgi-bin/show.py?" method="POST">"""
print "<input type=\"hidden\" name=\"nombre\" value=\"%s\" >" % (nombre)
print "<input type=\"hidden\" name=\"code\" value=\"%s\" >" % (code)
	   
print """<input type="submit" value="Volver">"""
print "</form>"

print "</body>"
print "</html>"

#!/usr/bin/python
# -*- coding: cp1252 -*-

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

#Creamos una lista con los nombre de las tablas
cursor.execute("SELECT name from sqlite_master WHERE type='table';")
aux = cursor.fetchall()
lista = []
for i in aux:
        lista.append(i[0])
#Código html para empezar la pagina web
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Lista de deseos:</title>"
print "</head>"
print "<body>"

#####print form ##### only for debugging
#Vamos recorriendo cada tabla de la db
for tabla in lista:
	if tabla != nombre.lower():
                #Creamos una lista con las ideas de cada tabla
		cursor.execute("SELECT * FROM %s" % (tabla.lower()) )
		ideas = cursor.fetchall()
		for i in ideas:
                        #Si las ideas están en form son porque tenían el bóton activado
			if i[0] in form:
                                #Actualizar el valor "asignado" de las ideas seleccionadas
				cursor.execute("UPDATE \"%s\" set asignado=\"%s\" where idea=\"%s\" " % (tabla, nombre.lower(), i[0]))
#Guardar y cerrar la db
db.commit()
db.close()
print "<h2> Asignado correcto </h2>"

#Generar botón de vuelta a show.py
print """<form action="/cgi-bin/show.py?" method="POST">"""
print "<input type=\"hidden\" name=\"nombre\" value=\"%s\" >" % (nombre)
print "<input type=\"hidden\" name=\"code\" value=\"%s\" >" % (code)
	   
print """<input type="submit" value="Volver">"""
print "</form>"

#Cerrar estructura de página html
print "</body>"
print "</html>"

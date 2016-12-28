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
code   = int(code)

#Crear claves de acceso. En este caso la clave es la primera letra del nombre en ASCII +100
key    = ord(nombre[0])+100

#Creamos una lista con los nombres de las tablas de la base de datos
cursor.execute("SELECT name from sqlite_master WHERE type='table';")
aux = cursor.fetchall()
lista = []
for i in aux:
        lista.append(i[0])
#Código HTML para iniciar una pagina web
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Lista de deseos:</title>"
print "</head>"
print "<body>"
#print "<h2>Code: %s Key: %s</h2>" % (code, key)  #only for debugging
#Comprobamos la clave introducida
if code==key:
    #print "<h2>Son iguales</h2>" #only for debbuging
    print """<form action="/cgi-bin/update.py " method="POST">"""
    for tabla in lista:
                #Creamos listas de todas las ideas de cada tabla
		print "<h2> Lista de %s:</h2>" % (tabla)
    		cursor.execute("SELECT * FROM %s" % (tabla.lower()) )
    		ideas = cursor.fetchall()
    		for i in ideas:
                        #Imprimimos las listas. Distiguiendo nuestra lista del resto
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
    #Cerramos la base de datos. Hemos terminado las operaciones (de lectura)
else:
    #Si la clave introducida es incorrecta
    print "<h2>Clave incorrecta.</h2>"

#Creamos un boton para volver al index.html
print """<form action="http://192.168.1.106" method="POST">
           <input type="submit" value="Volver">
         </form>"""
#Cerramos la estructura de la pagina web
print "</body>"
print "</html>"

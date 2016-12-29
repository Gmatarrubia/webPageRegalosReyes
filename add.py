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
idea   = form.getvalue('idea')
code   = int(code)
key    = ord(nombre[0])+100

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Tu lista de deseos</title>"
print "</head>"
print "<body>"
#print "<h2>Code: %s Key: %s</h2>" % (code, key)  #only for debugging
if code==key:
    #print "<h2>Son iguales</h2>" #only for debbuging
    print "<h2> Lista actualizada correctamente: </h2>"
    cursor.execute("INSERT INTO %s(idea,asignado) VALUES(\"%s\",\"nadie\")" % (nombre.lower(), idea))
    cursor.execute("SELECT * FROM %s" % (nombre.lower()) )
    ideas = cursor.fetchall()
    db.commit()
    db.close()
    for i in ideas:
        print "%s <br>" % (i[0])
else:
    print "<h2>Clave incorrecta.</h2>"

#Crear un boton para volver a index.html
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))

print "<form action=\"http://%s\" method=\"POST\">" % (s.getsockname()[0])
print """<input type="submit" value="Volver">
         </form>"""
s.close()
#########Metodo antiguo si se conoce la ip, no hace falta conexion a internet#####
#print """<form action="http://192.168.1.106" method="POST">
#           <input type="submit" value="Volver">
#         </form>"""
#Cerramos la estructura de la pagina web
##################################################################################
print "</body>"
print "</html>"

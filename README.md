# webPageRegalosReyes
Página incial en html y scripts en python para gestionar una base de datos web para los regalos de los reyes magos. <br> 
*El proyecto está pensado para alojarse en una raspberry pi.<br>

------------------
* Prerrequisitos *
------------------
Tener instalado y configurado sqlite3, apache y su módulo cgi para python. <br>
sudo apt-get install sqlite3 apache2 <br>

Para configurar cgi existen sencillos tutoriales que encontrarás fácilment en google. <br>

------------------
* Localizaciones *
------------------

/var/www/html/index.html <br> <br>

/usr/lib/cgi-bin/add.py <br>
                /show.py <br>
                /update.py <br>
                
--------------------
* Puesta en marcha *
--------------------

<h3>(1)Encender el servicio de apache con:</h3>
sudo service apache2 start

<h3>(2)Llenar la db con tantas tablas como personas</h3>
..../ sqlite3 lista.db <br>
CREATE TABLE nombre1(idea TEXT, asignado TEXT); <br>
CREATE TABLE nombre2(idea TEXT, asignado TEXT); <br>
...
...

<h3>(3)Modificar en el index.htlm</h3>
Añadiendo/modificando los nombres. Dejando así los mismos nombres que los creados en la base de datos.

<h3>(4)Dar permisos de escritura al directorio de la db </h3>
sudo chmod 777 /usr/lib/cgi-bin/

<h3>(5)¡Listo! Entra con un navegador en la dirección ip de tu raspberry pi.</h3>


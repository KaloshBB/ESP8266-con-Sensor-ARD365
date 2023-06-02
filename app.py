import socket
import time
import mysql.connector
#import main

#Establecer conexion con la base de datos
cnx = mysql.connector.connect(
    host='La direccion ip del host',
    user='nombre del usuario',
    password='contraseña del usuario',
    database='nombre de la base de datos',
    port=#numero de puerto
)
cursor = cnx.cursor()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#numpuerto debe ser reemplazado con el numero de puerto que se desea utilizar
s.bind(('direccion ipv4 de la computadora', numpuerto))

s.listen(0)
    #establece la conexion con el cliente

while True:
    
    client, addr = s.accept()
    
    client.settimeout(5)
    while True:
        content = client.recv(1024)
        
        if len(content) == 0:
            break
        if str(content, 'utf-8') == '\r\n':
            continue
        else:
        #imprime los datos recibidos del cliente
            print(str(content, 'utf-8'))
        #envia un mensaje al cliente para verificar conexion
            client.send(b'Hello From Python')

        #almacena la cadena de texto que contiene el dato recibido dentro de una variable para posteriormente meterla dentro de la base de datos
        dato = str(content, 'utf-8').split(":")
        #parsea el tipo de dato recibido a entero
        data = int(dato[1])
        #saca la fecha actual del sistema y la almacena en una variable
        fecha_hora_actual = time.strftime("%Y-%m-%d %H:%M:%S")

        #esta es la consulta que se ejecutara dentro de la base de datos, se inserta la fecha y el dato recibido
        query = "INSERT INTO agua (fecha, nivel) VALUES (%s, %s)"
        #se ejecuta la consulta
        cursor.execute(query, (fecha_hora_actual, data))
        #se confirma la ejecucion de la consulta
        cnx.commit()
    #cierra la conexion con el cliente
    client.close()
#cierra la conexion con la base de datos
cursor.close()
cnx.close()

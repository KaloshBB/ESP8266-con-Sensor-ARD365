import socket
import time
import mysql.connector
import main


cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='nivelagua'
)
cursor = cnx.cursor()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.1.82', 8585))

s.listen(0)


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
            
            print(str(content, 'utf-8'))
            client.send(b'Hello From Python')

        dato = str(content, 'utf-8').split(":")
        data= int(dato[1])
        fecha_hora_actual = time.strftime("%Y-%m-%d %H:%M:%S")


        query = "INSERT INTO agua (fecha, nivel) VALUES (%s, %s)"
        #values = (fecha_hora_actual, dato)
        cursor.execute(query, (fecha_hora_actual, data))
        cnx.commit()
        main.run_discord_bot()

    client.close()


cursor.close()
cnx.close()
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

#Este archivo se encarga de graficar los datos almacenados en la base de datos, se ejecuta en la clase bot.py
#Se establece esta funcion para poder ejecutarla en la clase bot.py
def graficar():
    file_name = 'nivelagua.csv'

#establece conexion con la base de datos
try:
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='nivelagua'
    )
    cursor = cnx.cursor()

    # Crear un objeto SQLAlchemy Engine
    #MODIFICAR ESTA LINEA CON LAS CREDENCIALES DEL SERVER DE TU BASE DE DATOS PARA QUE FUNCIONE
    engine = create_engine('mysql+mysqlconnector://usuario:contraseña@host/basededatos')

    #La consulta puede ser modificada para que se grafiquen los datos que se deseen, por ejemplo en el between se puede modificar la fecha para que se grafiquen los datos de un dia en especifico.
    query = "SELECT nivel, fecha FROM agua WHERE fecha BETWEEN '2023-05-31 00:00:00' AND '2023-06-01 23:59:59'"
    
    df = pd.read_sql(query, con=engine)
    df['fecha'] = pd.to_datetime(df['fecha'])
    plot = df.plot.density(x='fecha', y='nivel', title="ROTOPLAS", legend=False)
    #NO TENGO NI IDEA DE PORQUE LA GRAFICA LAS ETIQUTAS DEL EJE X SE VEN ASI, PERO FUNCIONA
    #Es el texto que saldra que representa el eje x y el eje y
    plt.xlabel("Tiempo")
    plt.ylabel("Densidad del agua")
    #no se :)
    plt.ylim(0, 0.01)  
    plt.xticks(rotation=45)  
    plt.yticks([0, 0.005, 0.01], ['0', '500', '1023']) 
    #guarda la grafica en la ruta especificada, tener cuidado donde la guardas porque el bot solo lee los datos de su misma carpeta del proyecto
    
    plt.savefig("/nivelagua.png")

except mysql.connector.Error as e:
    print(f"The error '{e}' occurred")
finally:
    if cnx.is_connected():
        cursor.close()
        cnx.close()


import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


def graficar():
    file_name = 'nivelagua.csv'
try:
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='nivelagua'
    )
    cursor = cnx.cursor()

    # Crear un objeto SQLAlchemy Engine
    engine = create_engine('mysql+mysqlconnector://root:root@localhost/nivelagua')

    query = "SELECT nivel, fecha FROM agua WHERE fecha BETWEEN '2023-05-31 00:00:00' AND '2023-06-01 23:59:59'"
    df = pd.read_sql(query, con=engine)
    df['fecha'] = pd.to_datetime(df['fecha'])
    plot = df.plot.density(x='fecha', y='nivel', title="ROTOPLAS", legend=False)
    plt.xlabel("Tiempo")
    plt.ylabel("Densidad del agua")
    plt.ylim(0, 0.01)  # Ajusta los límites del eje y según tus datos
    plt.xticks(rotation=45)  # Rota las etiquetas del eje x para mayor legibilidad
    plt.yticks([0, 0.005, 0.01], ['0', '500', '1023'])  # Personaliza las etiquetas del eje y
    plt.savefig("C:/Users/Kalos/OneDrive/Escritorio/servidor/nivelagua.png")

except mysql.connector.Error as e:
    print(f"The error '{e}' occurred")
finally:
    if cnx.is_connected():
        cursor.close()
        cnx.close()


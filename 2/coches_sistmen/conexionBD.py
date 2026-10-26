import mysql.connector
try:
    conexion = mysql.connector.connect(

        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'bd_coches'
    )
    cursor = conexion.cursor(buffered=True)
except:
    print("por el momento no es posible conectarse con la base de datos  intentelo mas tarde")


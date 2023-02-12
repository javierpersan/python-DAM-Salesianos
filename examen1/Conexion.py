import MySQLdb
class Conexion:
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = ''
    DB_NAME = 'primitiva'

    def __init__(self,query=''):
        print("conexion abierta")
        datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]

        conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
        cursor = conn.cursor()  # Crear un cursor
        cursor.execute(query)  # Ejecutar una consulta

        if query.upper().startswith('SELECT'):
            data = cursor.fetchall()  # Traer los resultados de un select
        else:
            conn.commit()  # Hacer efectiva la escritura de datos
            data = None

        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        return data

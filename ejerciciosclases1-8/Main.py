import MySQLdb
class Conexion:

    def __init__(self):
        DB_HOST = 'localhost'
        DB_USER = 'root'
        DB_PASS = 'mysqlroot'
        DB_NAME = 'a'

    def run_query(self ,query=''):
            datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]

            conn = MySQLdb.connect(*datos)
            cursor = conn.cursor()
            cursor.execute(query)

            if query.upper().startswith('SELECT'):
                data = cursor.fetchall()
            else:
                conn.commit()
                data = None

            cursor.close()
            conn.close()

            return data
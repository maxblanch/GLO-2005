from flask import jsonify
from mysql.connector import MySQLConnection, Error

class CoworkingSpace:
    config = {
        'user': 'root',
        'password': 'glo2005',
        'host': 'localhost',
        'database': 'WeShare',
        'port': '3306'
    }
    

    def __init__(self):
        self.connector = None
        try:
            self.conn = MySQLConnection(**self.config)
            if self.conn.is_connected():
                print('Connected to MySql database')
        except Error as e:
            print(e)

    def get_all_cwspaces(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM CoworkingSpace")
            rows = cursor.fetchall()
            return jsonify(rows)
 
        except Error as e:
            print(e)
        
        finally:
            cursor.close()

        
    def get_cwspace(self, cwspace_id):
            try:
                cursor = self.conn.cursor()
                cursor.execute(f"SELECT * FROM CoworkingSpace WHERE cws_id = {cwspace_id}")
                row = cursor.fetchone()
                return jsonify(row)
    
            except Error as e:
                print(e)
            
            finally:
                cursor.close()
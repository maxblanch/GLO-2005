from flask import jsonify
from mysql.connector import MySQLConnection, Error

class Coworker:
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

    def get_coworkers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Coworker")
            rows = cursor.fetchall()
            return jsonify(rows)
 
        except Error as e:
            print(e)
        
        finally:
            cursor.close()

        
    def get_coworker(self, coworker_id):
            try:
                cursor = self.conn.cursor()
                cursor.execute(f"SELECT * FROM Coworker WHERE coworker_id = {coworker_id}")
                row = cursor.fetchone()
                return jsonify(row)
    
            except Error as e:
                print(e)
            
            finally:
                cursor.close()
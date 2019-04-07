from flask import jsonify
from mysql.connector import MySQLConnection, Error

class Review:
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

    def get_reviews(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Review")
            rows = cursor.fetchall()
            return jsonify(rows)
 
        except Error as e:
            print(e)
        
        finally:
            cursor.close()

        
    def get_review(self, cws_id, coworker_id):
            try:
                cursor = self.conn.cursor()
                cursor.execute(f"SELECT * FROM Review WHERE cws_id = {cws_id} AND coworker_id = {coworker_id}")
                row = cursor.fetchone()
                return jsonify(row)
    
            except Error as e:
                print(e)
            
            finally:
                cursor.close()
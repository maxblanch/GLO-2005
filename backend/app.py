from flask import Flask, request, jsonify
from mysql.connector import MySQLConnection, Error
from controllers.coworking_space import CoworkingSpace

app = Flask(__name__)

""" config = {
    'user': 'root',
    'password': 'glo2005',
    'host': 'localhost',
    'database': 'WeShare',
    'port': '3306'
}

def connect():
    # Connect to MySQL Database
    try:
        conn = MySQLConnection(**config)
        if conn.is_connected():
            print('Connected to MySql database')
            return conn
    except Error as e:
        print(e) """
""" connection = pymysql.connect(host='mysql',
                             user='root',
                             password='glo2005',
                             db='CONNECTD',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor) """


@app.route('/')
def hello():
    db = CoworkingSpace()
    return "Hello World from Docker!!!!"

@app.route('/cwspaces', methods=['GET'])
def get_cwspaces():
    return CoworkingSpace().get_all_cwspaces()

@app.route('/cwspaces/<id>', methods=['GET'])
def get_cwspace(id):
    return CoworkingSpace().get_cwspace(id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

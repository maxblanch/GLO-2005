from flask import Flask
from mysql.connector import connect
app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'glo2005',
    'host': 'localhost',
    'database': 'WeShare',
    'port': '3306'
}

cnx = connect(**config)
""" connection = pymysql.connect(host='mysql',
                             user='root',
                             password='glo2005',
                             db='CONNECTD',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor) """

@app.route('/')
def hello():
    return "Hello World from Docker!!!!"

@app.route('/test')
def test():
    return "This is a test!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask
import pymysql.cursors
app = Flask(__name__)

connection = pymysql.connect(host='mysql',
                             user='root',
                             password='glo2005',
                             db='CONNECTD',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def hello():
    return "Hello World from Docker!!!!"

@app.route('/test')
def test():
    return "This is a test!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
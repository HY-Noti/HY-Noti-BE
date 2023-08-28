from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import pymysql
import yaml

app = Flask(__name__)
CORS(app)

with open('secrets.yaml', 'r') as file:
    secrets = yaml.safe_load(file)

db_pw = secrets['db_pw']

# MySQL 연결을 위한 함수
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd=str(db_pw),
        db='HY_noti',
        charset='utf8')

@app.route('/hynoti/hyin', methods=['POST'])
def hy_in():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM HY_in"
            cursor.execute(sql)
            rows = cursor.fetchall()
            data_list = []
            for row in rows:
                data = {
                    'num': row[0],
                    'cate': row[1],
                    'time': row[2],
                    'writer': row[3],
                    'title': row[4],
                    'main': row[5],
                    'url': row[6],
                    'file': row[7]
                }
                data_list.append(data)
            return jsonify(data_list)
    finally:
        connection.close()

@app.route('/hynoti/hyie', methods=['POST'])
def hy_ie():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM HY_ie"
            cursor.execute(sql)
            rows = cursor.fetchall()
            data_list = []
            for row in rows:
                data = {
                    'num': row[0],
                    'cate': row[1],
                    'time': row[2],
                    'writer': row[3],
                    'title': row[4],
                    'main': row[5],
                    'url': row[6],
                    'file': row[7]
                }
                data_list.append(data)
            return jsonify(data_list)
    finally:
        connection.close()

@app.route('/hynoti/chat', methods=['POST'])
def make_chat():
    return 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

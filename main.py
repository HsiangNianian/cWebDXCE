from flask import Flask, request, jsonify
import os
import sqlite3
import time
import random

app = Flask(__name__, static_folder='static')

DATABASE = 'database/data.db'


def create_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Dice (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                sides INTEGER,
                created_at INTEGER
            )'''
        )


def insert_dice(name, sides):
    created_at = int(time.time())
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO Dice (name, sides, created_at) VALUES (?, ?, ?)',
            (name, sides, created_at)
        )
        conn.commit()


def select_all_dice():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Dice')
        result = cursor.fetchall()
    return result

# 获取所有骰子


def get_dice():
    db = get_db()
    dice = db.execute('SELECT * FROM Dice').fetchall()
    db.close()
    result = []
    for d in dice:
        result.append({
            'id': d['id'],
            'name': d['name'],
            'sides': d['sides'],
            'created_at': d['created_at']
        })
    return jsonify(result)

# 新增一个骰子


def add_dice():
    data = request.get_json()
    db = get_db()
    db.execute('INSERT INTO Dice (name, sides, created_at) VALUES (?, ?, ?)',
               [data['name'], data['sides'], int(time.time())])
    db.commit()
    db.close()
    return jsonify({'message': 'Dice added successfully!'})

# 删除一个骰子


def delete_dice(id):
    db = get_db()
    db.execute('DELETE FROM Dice WHERE id = ?', [id])
    db.commit()
    db.close()
    return jsonify({'message': 'Dice deleted successfully!'})

# 连接数据库


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

# 投掷一个骰子并返回结果


def roll_dice(id):
    db = get_db()
    dice = db.execute('SELECT * FROM Dice WHERE id = ?', [id]).fetchone()
    db.close()
    if dice is None:
        return jsonify({'error': 'Dice not found!'}), 404
    result = random.randint(1, dice['sides'])
    return jsonify({'result': result})


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/dice', methods=['GET', 'POST'])  # type: ignore
def dice():
    if request.method == 'GET':
        return get_dice()
    elif request.method == 'POST':
        return add_dice()


@app.route('/dice/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_dice(id)


@app.route('/roll/<int:id>', methods=['GET'])
def roll(id):
    return roll_dice(id)


if __name__ == '__main__':
    create_table()
    insert_dice('D6', 6)
    insert_dice('D10', 10)
    insert_dice('D12', 12)
    insert_dice('D20', 20)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

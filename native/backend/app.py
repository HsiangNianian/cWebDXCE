from flask import Flask, jsonify, request
import sqlite3
import random
import time

app = Flask(__name__,static_folder='../frontend')

DATABASE = 'database/dice.db'

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
        
# 连接数据库
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def index():
    return app.send_static_file('index.html')

# 获取所有骰子
@app.route('/api/dice', methods=['GET'])
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
@app.route('/api/dice', methods=['POST'])
def add_dice():
    data = request.get_json()
    db = get_db()
    db.execute('INSERT INTO Dice (name, sides, created_at) VALUES (?, ?, ?)',
               [data['name'], data['sides'], int(time.time())])
    db.commit()
    db.close()
    return jsonify({'message': 'Dice added successfully!'})

# 删除一个骰子
@app.route('/api/dice/<int:id>', methods=['DELETE'])
def delete_dice(id):
    db = get_db()
    db.execute('DELETE FROM Dice WHERE id = ?', [id])
    db.commit()
    db.close()
    return jsonify({'message': 'Dice deleted successfully!'})

# 投掷一个骰子并返回结果
@app.route('/api/roll/<int:id>', methods=['GET'])
def roll_dice(id):
    db = get_db()
    dice = db.execute('SELECT * FROM Dice WHERE id = ?', [id]).fetchone()
    db.close()
    if dice is None:
        return jsonify({'error': 'Dice not found!'}), 404
    result = random.randint(1, dice['sides'])
    return jsonify({'result': result})

if __name__ == '__main__':
    create_table()
    insert_dice('D6', 6)
    insert_dice('D10', 10)
    insert_dice('D12', 12)
    insert_dice('D20', 20)
    result = select_all_dice()
    for row in result:
        print(row)
    app.run(debug=True)
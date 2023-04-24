from flask import jsonify, request
import sqlite3
import random
import time

DATABASE = '../database/data.db'

# 连接数据库
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

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

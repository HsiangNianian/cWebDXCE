from flask import jsonify, request
import sqlite3
import random
import time

DATABASE = 'database/dice.db'

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

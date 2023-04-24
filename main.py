from flask import Flask, request
from api.roll import roll_dice
from api.dice import get_dice, add_dice, delete_dice
import os
import sqlite3
import time

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

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/dice', methods=['GET', 'POST']) # type: ignore
def dice():
    if request.method == 'GET':
        return get_dice()
    elif request.method == 'POST':
        return add_dice()

@app.route('/api/dice/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_dice(id)

@app.route('/api/roll/<int:id>', methods=['GET'])
def roll(id):
    return roll_dice(id)
        
if __name__ == '__main__':
    create_table()
    insert_dice('D6', 6)
    insert_dice('D10', 10)
    insert_dice('D12', 12)
    insert_dice('D20', 20)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

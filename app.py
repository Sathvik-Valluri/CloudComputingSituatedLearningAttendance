from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS attendance 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, emp_name TEXT, date TEXT, time TEXT, work_mode TEXT)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS leaves 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, emp_name TEXT, start_date TEXT, end_date TEXT, reason TEXT)''')
init_db()

@app.route('/')
def index():
    # Fetch data to display on the dashboard
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM attendance ORDER BY id DESC LIMIT 5")
        recent_attendance = cur.fetchall()
        cur.execute("SELECT * FROM leaves ORDER BY id DESC LIMIT 5")
        recent_leaves = cur.fetchall()
    return render_template('index.html', attendance=recent_attendance, leaves=recent_leaves)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    emp_name = request.form['emp_name']
    work_mode = request.form['work_mode']
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO attendance (emp_name, date, time, work_mode) VALUES (?, ?, ?, ?)", 
                    (emp_name, date, time, work_mode))
    return redirect(url_for('index'))

@app.route('/apply_leave', methods=['POST'])
def apply_leave():
    emp_name = request.form['emp_name']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    reason = request.form['reason']
    
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO leaves (emp_name, start_date, end_date, reason) VALUES (?, ?, ?, ?)", 
                    (emp_name, start_date, end_date, reason))
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Running on 0.0.0.0 allows external access when deployed
    app.run(host='0.0.0.0', port=80, debug=True)
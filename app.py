from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_latest_readings(limit=20):
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, power, temperature FROM sensor_readings
        ORDER BY timestamp DESC LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows[::-1]  # reverse to show oldest first

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    readings = get_latest_readings()
    return jsonify([
        {'timestamp': row[0], 'power': row[1], 'temperature': row[2]}
        for row in readings
    ])

if __name__ == '__main__':
    app.run(debug=True)

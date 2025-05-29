import time

import requests
import sqlite3

url = "http://192.168.1.152/report"
while True:
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to get sensor data: " + response.status_code)
        exit()

    data = response.json()

    database = sqlite3.connect("sensor_data.db")
    cursor = database.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            power REAL,
            ws REAL,
            relay BOOLEAN,
            temperature REAL,
            boot_id TEXT,
            energy_since_boot REAL,
            time_since_boot INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        INSERT INTO sensor_readings (
            power, ws, relay, temperature, boot_id, energy_since_boot, time_since_boot
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data["power"],
        data["Ws"],
        data["relay"],
        data["temperature"],
        data["boot_id"],
        data["energy_since_boot"],
        data["time_since_boot"]
    ))

    database.commit()
    database.close()

    print("Done")
    time.sleep(5)
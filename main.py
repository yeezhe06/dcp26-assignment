
import csv
import sqlite3

connection = sqlite3.connect("daily_routine.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS daily_routine (
    date TEXT,
    sleep_hours TEXT,
    sleeping_time TEXT,
    wake_up_time TEXT,
    meals_count INTEGER,
    weather TEXT,
    bus_time_to_school TEXT,
    back_to_home TEXT
)
""")

with open("data/daily_routine.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        connection.execute("""
        INSERT INTO daily_routine
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["date"],
            row["sleep_hours"],
            row["sleeping_time"],
            row["wake_up_time"],
            int(row["meals_count"]),
            row["weather"],
            row["bus_time to school"],
            row["back to home"]
        ))

connection.commit()
connection.close()

print("Data saved to SQLite successfully!")

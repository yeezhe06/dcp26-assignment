
import csv
import sqlite3

# Connect to the database
connection = sqlite3.connect("daily_routine.db")

# Create a table
connection.execute("""
CREATE TABLE IF NOT EXISTS daily_routine (
    date TEXT,
    sleep_hours REAL,
    wake_up_time TEXT,
    screen_time_hours REAL,
    meals_count INTEGER,
    weather TEXT,
    bus time to school INTEGER,
    back to home INTEGER
)
""")

# Read the CSV file
with open("data/daily_routine.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        connection.execute("""
        INSERT INTO daily_routine
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["date"],
            float(row["sleep_hours"]),
            row["wake_up_time"],
            float(row["screen_time_hours"]),
            int(row["meals_count"]),
            row["weather"],
            int(row["bus time to school"]),
            int(row["back to home"])
        ))

connection.commit()
connection.close()

print("Data saved to SQLite successfully!")


import csv
import sqlite3

connection = sqlite3.connect("daily_routine.db")

connection.execute("DELETE FROM daily_routine")

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
            row["Date"],
            row["sleep_hours"],
            row["sleeping_time"],
            row["wake_up_time"],
            int(row["meals_count"]),
            row["weather"],
            row["bus_time_to_school"],
            row["back_to_home"]
        ))


dta = connection.execute("""
SELECT * FROM daily_routine
""")

for row in dta:
    print(row)

dta = connection.execute("""
SELECT Count(*) FROM daily_routine
""")

print("Total records:", dta.fetchone()[0])
 
dta = connection.execute("""
SELECT  * FROM daily_routine 
where weather = 'sunny day'
""")

print("\n Sunny Daysssss")

for row in dta:
    print(row)

dta = connection.execute("""
SELECT *FROM daily_routine
order by meals_count ASC
""")

print("\n meals increase")

for row in dta:
    print(row)

connection.commit()
connection.close()


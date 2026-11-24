import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

df =  pd.read_csv("data/daily_routine.csv")

print("\n Daily RouTine Data")
df.info()
print(df)

average_meals = df["meals_count"].mean()

print("\nAverage Number of Meals:")
print(average_meals)

weather_count = df["weather"].value_counts()

print("\nWeather Count:")
print(weather_count)


#weather graph
df["weather"] = df["weather"].str.lower()

count = df["weather"].value_counts().head(10)
print(count)

plt.bar(count.index,count.values)
plt.title("weather Record")
plt.xlabel("weather type")
plt.ylabel("Numbers of Days")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()  
plt.savefig("setp2.png")             
plt.show()

#meals graph
count = df["meals_count"].value_counts().sort_index()
print(count)

plt.bar(count.index,count.values)
plt.title("Meals record")
plt.xlabel("Number of meals")
plt.ylabel("Numbers of Days")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()  
plt.savefig("step3.png")             
plt.show()


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

connection.execute("DELETE FROM daily_routine")

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

connection.commit()

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

connection.close()


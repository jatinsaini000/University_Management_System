import sqlite3
import os

# Create database in the user's home directory
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')

print(f"Creating database at: {db_path}")

# Create/connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables
cursor.execute("CREATE TABLE IF NOT EXISTS college (code INTEGER PRIMARY KEY, cname TEXT, city TEXT, courses INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS uit (sn INTEGER PRIMARY KEY, course TEXT, seats INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS uit_student (enroll INTEGER PRIMARY KEY, name TEXT, branch TEXT, gender TEXT, mobile INTEGER, blood_g TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS marksheet (roll_number INTEGER PRIMARY KEY, name TEXT, father_name TEXT, mother_name TEXT, dob TEXT, gender TEXT, subject1 INTEGER, subject2 INTEGER, subject3 INTEGER, subject4 INTEGER, subject5 INTEGER, total INTEGER, percentage REAL, grade TEXT)")

# Save changes and close connection
conn.commit()
conn.close()

print("Database and tables created successfully!") 
import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

# Create table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS college (code INTEGER PRIMARY KEY, cname TEXT, city TEXT, courses INTEGER)")

# Add the three universities
colleges = [
    (1001, "Rayat Bahra University", "Mohali", 10),
    (1002, "Chandigarh University", "Mohali", 12),
    (1003, "Punjab University", "Chandigarh", 15)
]

# Insert the colleges
for college in colleges:
    try:
        cur.execute("INSERT INTO college VALUES (?, ?, ?, ?)", college)
        print(f"Added {college[1]} successfully!")
    except sqlite3.IntegrityError:
        print(f"{college[1]} already exists in database")

con.commit()
con.close()

print("\nAll colleges have been added to the database!") 
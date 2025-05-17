import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

q = "CREATE TABLE IF NOT EXISTS collage (code INTEGER PRIMARY KEY, cname TEXT, city TEXT, courses INTEGER)"

cur.execute(q)

print("table created")
con.commit()






































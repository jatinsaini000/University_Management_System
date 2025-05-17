import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

def collegeTB():
    q = "CREATE TABLE IF NOT EXISTS college (code INTEGER PRIMARY KEY, cname TEXT, city TEXT, courses INTEGER)"
    cur.execute(q)
    print("\n\nTable Created")
    con.commit()

def uitTB():
    q="create table uit(sn int primary key,course varchar(20),seats int)"
    cur.execute(q,)
    print("\n\nTable Created")


def createTB_for_uit_students():
    q="create table uit_student(enroll int primary key,name varchar(30),branch varchar(30),gender varchar(10),mobile int,blood_g varchar(6))"
    cur.execute(q,)
    print("\n\nTable created")










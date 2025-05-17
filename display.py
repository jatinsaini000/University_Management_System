import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

def display_college():
    q="select*from college"
    cur.execute(q)
    print("\n\n+++++++LIST OF COLLEGES+++++++++\n\n")
    for i in cur:
        print(" CODE","COLLEGE ","CITY","COURSES")
        print(i)
        print("="*120)
    con.commit()

def display_uit():
    q="select*from uit"
    cur.execute(q)
    print("\n\n+++++++List Of Branches And Total Seats in UIT+++++++\n\n")
    for i in cur:
        print("S.N.","   Branch","  Total")
        print(i)
        print("="*120)
    con.commit()

def display_uit_student():
    q="select*from uit_student"
    cur.execute(q)
    print("\n\n+++++++List Of Student in UIT+++++++\n\n")
    for i in cur:
        print(" ENROLL","     NAME  ","      BRANCH","   GENDER","  B_G","     MOBILE")
        print(i)
        print("="*120)
    con.commit()






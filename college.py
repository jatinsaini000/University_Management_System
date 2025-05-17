import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

def search_into_college1():
    d = input("\n\nEnter college name:\t")
    q = "SELECT * FROM college WHERE cname=?"
    t = (d,)
    cur.execute(q, t)
    for i in cur:
        print("\n\nCollege Code:\t", i[0])
        print("College Name:\t", i[1])
        print("City:\t\t", i[2])
        print("Courses:\t", i[3])
        print("=" * 120)
    con.commit()

def search_into_college2():
    d = int(input("\n\nEnter college code:\t"))
    q = "SELECT * FROM college WHERE code=?"
    t = (d,)
    cur.execute(q, t)
    for i in cur:
        print("\n\nCollege Code:\t", i[0])
        print("College Name:\t", i[1])
        print("City:\t\t", i[2])
        print("Courses:\t", i[3])
        print("=" * 120)
    con.commit()

def search_into_uit_student1():
    d = int(input("\n\nEnter Enrollment number:\t"))
    q = "SELECT * FROM uit_student WHERE enroll=?"
    t = (d,)
    cur.execute(q, t)
    for i in cur:
        print("\n\nEnrollment Number:\t", i[0])
        print("Name:\t\t\t", i[1])
        print("Branch:\t\t\t", i[2])
        print("Gender:\t\t\t", i[3])
        print("Blood Group:\t\t", i[5])
        print("Mobile Number:\t\t", i[4])
        print("=" * 120)
    con.commit()

def search_into_uit_student2():
    d = input("\n\nEnter Student's Name:\t")
    q = "SELECT * FROM uit_student WHERE name=?"
    t = (d,)
    cur.execute(q, t)
    for i in cur:
        print("\n\nEnrollment Number:\t", i[0])
        print("Name:\t\t\t", i[1])
        print("Branch:\t\t\t", i[2])
        print("Gender:\t\t\t", i[3])
        print("Blood Group:\t\t", i[5])
        print("Mobile Number:\t\t", i[4])
        print("=" * 120)
    con.commit()

def search_into_uit_student3():
    d = int(input("\n\nEnter Student's mobile number:\t"))
    q = "SELECT * FROM uit_student WHERE mobile=?"
    t = (d,)
    cur.execute(q, t)
    for i in cur:
        print("\n\nEnrollment Number:\t", i[0])
        print("Name:\t\t\t", i[1])
        print("Branch:\t\t\t", i[2])
        print("Gender:\t\t\t", i[3])
        print("Blood Group:\t\t", i[5])
        print("Mobile Number:\t\t", i[4])
        print("=" * 120)
    con.commit()











    

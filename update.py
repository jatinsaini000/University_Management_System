import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

def update_in_collage1():
    u1=int(input("\n\nEnter code in which you want to update?\t"))
    u2=input("Enter college name you want to update\t")
    q=("update college set cname = ? where code=?")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")


def update_in_collage2():
    u1=int(input("\n\nEnter code in which you want to update?\t"))
    u2=input("Enter courses you want to update\t")
    q=("update college set courses = ? where code=?")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")

def update_in_uit():
    u1=int(input("\n\nEnter Serial Number in which you want to update?\t"))
    u2=input("Enter seats you want to update\t")
    q=("update uit set seats = ? where sn=?")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")
    
def update_in_uit_student1():
    u1=int(input("\n\nEnter Enrollment Number in which you want to do updation?\t"))
    u2=input("Enter branch name you want to update\t")
    q=("update uit_student set branch = ? where enroll=?")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")

def update_in_uit_student2():
    u1=int(input("\n\nEnter Enrollment Number in which you want to do updation?\t"))
    u2=input("Enter Blood Group you want to update\t")
    q=("update uit_student set blood_g = ? where enroll=?")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")

def update_in_uit_student3():
    u1=int(input("\n\nEnter Enrollment Number in which you want to do updation?\t"))
    u2=input("Enter Mobile Number which you want to update\t")
    q=("update uit_student set mobile= ? where enroll=?")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")

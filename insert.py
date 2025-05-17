import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()




def insert_into_collage():
    a=int(input("\n\nHow many records you want to insert in COLLEGE's database?\t"))
    for i in range(a):
        code=int(input("\n\nEnter college code:\t"))
        cname=input("Enter college Name:\t")
        city=input("Enter city of college:\t")
        courses=int(input("Enter total courses available in college:\t"))
        q="insert into college values(%s,%s,%s,%s)"
        t=(code,cname,city,courses)
        cur.execute(q,t)
        con.commit()
        print("\n\nData Inserted Successfully")



        
def insert_into_uit():
    a=int(input("\n\nHow many records you want to insert in UIT's database?\t"))
    for i in range(a):
        sn=int(input("\n\nEnter serial number:\t"))
        course=input("Enter course name:\t")
        seats=int(input("Enter total seats of course:\t"))
        q="insert into uit values(%s,%s,%s)"
        t=(sn,course,seats)
        cur.execute(q,t)
        con.commit()
        print("\n\nData Inserted Successfully")


def insert_into_uit_students():
    a=int(input("\n\nHow many records you want to insert in UIT's Student database?\t"))
    for i in range(a):
        enroll=int(input("\n\nEnter Enrollment number:\t"))
        name=input("Enter Student's name:\t")
        branch=input("Enter Student's Branch:\t")
        gender=input("Enter Student's Gender:\t")
        blood_g=input("Enter Student's Blood Group:\t")
        mobile=int(input("Enter Student's mobile number:\t"))
        q="insert into uit_student values(%s,%s,%s,%s,%s,%s)"
        t=(enroll,name,branch,gender,blood_g,mobile)
        cur.execute(q,t)
        con.commit()
        print("\n\nData Inserted Successfully")



import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

# Create table if it doesn't exist
cur.execute("""CREATE TABLE IF NOT EXISTS uit_student 
               (enroll int primary key, name varchar(30), branch varchar(30), 
                gender varchar(10), mobile int, blood_g varchar(6))""")

# Add sample students
students = [
    (10001, "Rahul Sharma", "Computer Science", "Male", 9876543210, "O+"),
    (10002, "Priya Patel", "Electronics", "Female", 9876543211, "A+"),
    (10003, "Amit Kumar", "Mechanical", "Male", 9876543212, "B+"),
    (10004, "Neha Singh", "Computer Science", "Female", 9876543213, "AB+"),
    (10005, "Vikram Malhotra", "Civil", "Male", 9876543214, "O-"),
    (10006, "Ananya Gupta", "Electronics", "Female", 9876543215, "A-"),
    (10007, "Rajesh Verma", "Mechanical", "Male", 9876543216, "B-"),
    (10008, "Sneha Reddy", "Computer Science", "Female", 9876543217, "O+"),
    (10009, "Karan Mehta", "Civil", "Male", 9876543218, "A+"),
    (10010, "Pooja Sharma", "Electronics", "Female", 9876543219, "B+")
]

# Insert the students
for student in students:
    try:
        cur.execute("INSERT INTO uit_student VALUES (?, ?, ?, ?, ?, ?)", student)
        print(f"Added student {student[1]} successfully!")
    except sqlite3.IntegrityError:
        print(f"Student {student[1]} already exists in database")

con.commit()
con.close()

print("\nAll students have been added to the database!") 
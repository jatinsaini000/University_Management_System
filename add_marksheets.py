import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

# Create marksheet table if it doesn't exist
cur.execute("""CREATE TABLE IF NOT EXISTS marksheet
               (roll_number bigint primary key, name varchar(20), fname varchar(20), 
                mname varchar(20), dob bigint, gender char, sub1 int, sub2 int, 
                sub3 int, sub4 int, sub5 int, total bigint, per int, grade char)""")

# Add sample marksheet entries
marksheets = [
    (10001, "Rahul Sharma", "Rajesh Sharma", "Meena Sharma", 20000101, "M", 85, 90, 88, 92, 87, 442, 88, "A"),
    (10002, "Priya Patel", "Ramesh Patel", "Sita Patel", 20000215, "F", 92, 88, 95, 89, 91, 455, 91, "A+"),
    (10003, "Amit Kumar", "Suresh Kumar", "Rekha Kumar", 20000320, "M", 78, 82, 85, 80, 79, 404, 81, "B+"),
    (10004, "Neha Singh", "Vikram Singh", "Anita Singh", 20000410, "F", 95, 93, 94, 96, 92, 470, 94, "A+"),
    (10005, "Vikram Malhotra", "Raj Malhotra", "Sunita Malhotra", 20000505, "M", 88, 85, 90, 87, 89, 439, 88, "A"),
    (10006, "Ananya Gupta", "Prakash Gupta", "Ritu Gupta", 20000625, "F", 91, 89, 93, 90, 92, 455, 91, "A+"),
    (10007, "Rajesh Verma", "Mohan Verma", "Geeta Verma", 20000715, "M", 82, 85, 80, 83, 84, 414, 83, "B+"),
    (10008, "Sneha Reddy", "Krishna Reddy", "Lakshmi Reddy", 20000820, "F", 89, 92, 88, 90, 91, 450, 90, "A+"),
    (10009, "Karan Mehta", "Dinesh Mehta", "Pooja Mehta", 20000910, "M", 86, 88, 85, 87, 89, 435, 87, "A"),
    (10010, "Pooja Sharma", "Ravi Sharma", "Neetu Sharma", 20001005, "F", 93, 91, 94, 92, 90, 460, 92, "A+")
]

# Insert the marksheet entries
for marksheet in marksheets:
    try:
        cur.execute("INSERT INTO marksheet VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", marksheet)
        print(f"Added marksheet for {marksheet[1]} successfully!")
    except sqlite3.IntegrityError:
        print(f"Marksheet for {marksheet[1]} already exists in database")

con.commit()
con.close()

print("\nAll marksheets have been added to the database!") 
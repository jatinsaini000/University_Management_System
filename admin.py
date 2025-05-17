import sqlite3
import os

# Connect to SQLite database
home_dir = os.path.expanduser("~")
db_path = os.path.join(home_dir, 'university.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

print('''
        |     |  |\   |   -----  \        /  -----  ------  -----  ------  -------  \     /
        |     |  | \  |     |     \      /   |      |    |  |         |       |      \   /
        |     |  |  \ |     |      \    /    -----   ----   |         |       |       \ /
        |     |  |   \|     |       \  /     |      | \     |         |       |        /
         -----            -----      \/      -----  |  \    -----  ------     |       /  


        |\    /|     /\     |\    |     /\     ------   ------  |\    /|  ------  |\    |  --------
        | \  / |    /  \    | \   |    /  \    |        |       | \  / |  |       | \   |      |
        |  \/  |   /----\   |  \  |   /----\   |  |--|   ----   |  \/  |   ----   |  \  |      |
        |      |  /      \  |   \ |  /      \  |  |  |  |       |      |  |       |   \ |      |   
        |      | /        \ |    \| /        \ |--|  |   ----   |      |   -----  |    \|      |     

        --------  \      /   --------  -------   ---------   |\    /|
        |          \    /    |            |      |           | \  / |
        |______     \  /     |______      |      |_______    |  \/  |
               |     \/             |     |      |           |      |
               |     /              |     |      |           |      |
        --------    /        --------     |      --------    |      |
        ''')

# Get list of tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
for table in tables:
    print(table[0])

print("="*78)
print("1)Search for a colleges in University Database ")
print("2)For Update in a college Database ")
print("3)Insert New college in University Database")
print("4)Delete college from University Database")
print("5)Show list of Colleges")
print("6)Search for student in college Database ")
print("7)Insert New Student in college Database")
print("8)Delete New student from college Database")
print("9)Show list of Students")
print("10)To Exit type 'EXIT' or 'exit'")











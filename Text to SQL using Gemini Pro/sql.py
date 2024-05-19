import sqlite3


connection=sqlite3.connect("student.db")

## Create a curosr object to insert record, create table and retrieve
cursor=connection.cursor()

## Create the table
table_info="""Create table Student (NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);"""

cursor.execute(table_info)

cursor.execute("""Insert Into STUDENT values("Krish","Data Science","A",90)""")

cursor.execute("""Insert Into STUDENT values("Sudanshu","Data Science","B",100)""")

cursor.execute("""Insert Into STUDENT values("Darlus","Data Science","A",86)""")

cursor.execute("""Insert Into STUDENT values("Vikash","Devops","A",50)""")

cursor.execute("""Insert Into STUDENT values("Dipesh","Devops","A",35)""")

#display all the records
print("The inserted record are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close()


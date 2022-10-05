# 5. Provide a program to create tables (Employee, Department,
# Project) in database Sqlite and insert the data.
# • Make sure to add basic field, with employee to department and project relation.
# • Make sure maintain M2M relation between employee and project.


import sqlite3
from sqlite3 import Error


# Create the table  
def create_table ():
    try :
        cursorObj.execute('''CREATE TABLE Employee(
                Employee Name char(30), 
                Dept Name char(35), 
                Project Name char(35),
                team_id INTEGER, 
                hero_id INTEGER, 
                PRIMARY KEY (team_id, hero_id));''')

        cursorObj.execute('''CREATE TABLE Department(
                Department  char(30), 
                Dept ID char(35), 
                Project nme char(35),
                team_id INTEGER, 
                hero_id INTEGER, 
                PRIMARY KEY (team_id, hero_id), 
                FOREIGN KEY(team_id) REFERENCES Employee (id), 
                FOREIGN KEY(hero_id) REFERENCES Employee (id));''')

        cursorObj.execute('''CREATE TABLE Project(
                Prjct Name  char(30), 
                Dept nme char(35), 
                Project char(35),
                team_id INTEGER, 
                hero_id INTEGER, 
                PRIMARY KEY (team_id, hero_id), 
                FOREIGN KEY(team_id) REFERENCES Employee (id), 
                FOREIGN KEY(hero_id) REFERENCES Employee (id));''')

    except Error:
        print(Error)

#Insert records
def insertrec():
    try:
        cursorObj.executescript("""
                INSERT INTO Employee VALUES( 'James Hoog', 'New York', 'dp',12,14);
                INSERT INTO Employee VALUES( 'Nail Knite', 'Paris', 'wv',13,164);
                INSERT INTO Employee VALUES( 'Pit Alex', 'London', 'dc',125,514);
                INSERT INTO Employee VALUES( 'Mc Lyon', 'Paris', "mcu",182,9149);
                INSERT INTO Employee VALUES( 'Paul Adam', 'Rome', 'ben10',1602,914);
                """)

        cursorObj.executescript("""
                INSERT INTO Project VALUES( 'James Hoog', 'New York', 'dp',12,14);
                INSERT INTO Project VALUES( 'Nail Knite', 'Paris', 'wv',13,164);
                INSERT INTO Project VALUES( 'Pit Alex', 'London', 'dc',125,514);
                INSERT INTO Project VALUES( 'Mc Lyon', 'Paris', "mcu",182,9149);
                INSERT INTO Project VALUES( 'Paul Adam', 'Rome', 'ben10',1602,914);
                """)

        cursorObj.executescript("""
                INSERT INTO Department VALUES( 'James Hoog', 'New York', 'dp',12,14);
                INSERT INTO Department VALUES( 'Nail Knite', 'Paris', 'wv',13,164);
                INSERT INTO Department VALUES( 'Pit Alex', 'London', 'dc',125,514);
                INSERT INTO Department VALUES( 'Mc Lyon', 'Paris', "mcu",182,9149);
                INSERT INTO Department VALUES( 'Paul Adam', 'Rome', 'ben10',1602,914);
                """)



        conn.commit()

        cursorObj.execute("SELECT * FROM Employee")
        rows = cursorObj.fetchall()
        print("Employee details:")
        for row in rows:
            print(row)

        cursorObj.execute("SELECT * FROM Project")
        rows = cursorObj.fetchall()
        print("Project details:")
        for row in rows:
            print(row)

        cursorObj.execute("SELECT * FROM Department")
        rows = cursorObj.fetchall()
        print("Department details:")
        for row in rows:
            print(row)

    except Error:
         print(Error)





#To input data row from user
def recinserter():
    try:
        c=input('Select table to insert data- \nE - For Employee \nD - For Department \nP - For Project  \n')

        if c=='E' or c=='e':
            d=int(input('Enter number of record rows to be inserted -  '))
            for i in range(d):
                print('Enter Employee Details')

                Emp  =input("Employee Name  ")
                Dpt  =input("Dept Name  ") 
                Prj =input("Project Name  ") 
                tm = input("Team ID  ") 
                hr =input("Hero ID  ") 

                

                # This is the qmark style:
                cursorObj.execute("insert into Employee values (?, ?,?,?,?)", (Emp, Dpt,Prj, tm,hr))
                conn.commit()

            cursorObj.execute("SELECT * FROM Employee")
            rows = cursorObj.fetchall()
            print("Agent details:")
            for row in rows:
                print(row)


        if c=='D' or c == 'd':
            d=int(input('Enter number of record rows to be inserted -  '))
            for i in range(d):
                print('Enter Department Details')

                Emp  =input("Department  ")
                Dpt  =input("Dept ID  ") 
                Prj =input("Project Name  ") 
                tm = input("Team ID  ") 
                hr =input("Hero ID  ") 
                                                

                # This is the qmark style:
                cursorObj.execute("insert into Department values (?, ?,?,?,?)", (Emp, Dpt,Prj, tm,hr))
                conn.commit()

            cursorObj.execute("SELECT * FROM Department")
            rows = cursorObj.fetchall()
            print("Dept. details:")
            for row in rows:
                print(row)



        if c=='P' or c == 'p':
            d=int(input('Enter number of record rows to be inserted -  '))
            for i in range(d):
                print('Enter Project Details')

                Emp  =input("Prjct Name  ")
                Dpt  =input("Dept nme  ") 
                Prj =input("Project Name  ") 
                tm = input("Team ID  ") 
                hr =input("Hero ID  ")                                           

                # This is the qmark style:
                cursorObj.execute("insert into Department values (?, ?,?,?,?)", (Emp, Dpt,Prj, tm,hr))
                conn.commit()

               
            cursorObj.execute("SELECT * FROM Project")
            rows = cursorObj.fetchall()
            print("Dept. details:")
            for row in rows:
                print(row)

    except Error:
            print(Error)




#To read db
def reader():
    cursorObj.execute("SELECT * FROM Employee")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)

    cursorObj.execute("SELECT * FROM Project")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)

    cursorObj.execute("SELECT * FROM Department")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)



#driver code
# sqllite_conn = sql_connection()
# sql_table(sqllite_conn)
conn = sqlite3.connect('mydb1.db')
cursorObj = conn.cursor()


while True:
    try:
        df= input('To create tables enter - C \nTo insert default rows in the table enter - Y \nTo insert new rows in the table enter - N  \nTo view the table enter - V \nTo close the connection - E     ')
        if df == 'N' or df == 'n':
            insertrec=recinserter()
        if df == 'C' or df == 'c':
            createtable=create_table()
        elif df == 'Y' or df == 'y':
            insertrec=insertrec()
        elif df == 'V' or df == 'v':
            insertrec=reader()
        elif df== "E" or df == "e":
            conn.close()
        print("\nThe SQLite connection is closed.")

    except Exception as e:
        print(e)
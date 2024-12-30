import mysql.connector as sqltor

user_database = "root"
pwd_database = "#12tabparv"


def connect_to_db():
    """
    Establish a connection to the MySQL database.
    Returns:
            conn: MySQL connection object
    """
    conn = sqltor.connect(
        host="localhost",
        user=user_database,
        password=pwd_database, port="3306"
    )
    return conn


def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute("create table if not exists bus(busno int primary key, origin varchar(20), Dest varchar(20), Rate int, Km int)")
    conn.commit()
    cursor.close()
    conn.close()
    print("This was executed")


def insert_value():
    busno = int(input("Please enter the bus no.: "))
    origin = input("Please enter the starting point:  ")
    dest = input("Please enter the destination:  ")
    rate = int(input("Please enter the rate: "))
    km = int(input("Please enter the distance: "))
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute("insert into bus values( %s ,%s,%s,%s,%s)", [busno, origin, dest, rate, km])
    conn.commit()
    cursor.close()
    conn.close()


def display():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute("select * from bus;")
    tasks = cursor.fetchall()
    print(tasks)
    conn.commit()
    cursor.close()
    conn.close()





create_table()
while True:
    print("\n> MAIN MENU")
    print("[1] Add new Bus.")
    print("[2] View all Buses.")
    print("[3] Exit.")
    choice2 = int(input("Desired operation: [1/2/3] "))
    if choice2 == 1:
        insert_value()
    elif choice2 == 2:
        display()
    elif choice2 == 3:
        break
    else:
        print("Invalid Choice")

'''
This was executed

> MAIN MENU
[1] Add new Bus.
[2] View all Buses.
[3] Exit.
Desired operation: [1/2/3] 1
Please enter the bus no.: 1
Please enter the starting point:  delhi
Please enter the destination:  noida
Please enter the rate: 500
Please enter the distance: 50

> MAIN MENU
[1] Add new Bus.
[2] View all Buses.
[3] Exit.
Desired operation: [1/2/3] 2
[(1, 'delhi', 'noida', 500, 50)]

> MAIN MENU
[1] Add new Bus.
[2] View all Buses.
[3] Exit.
Desired operation: [1/2/3] 3

Process finished with exit code 0
'''

import mysql.connector as sqltor

user_database = "root"
pwd_database = "amity"


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
    cursor.execute("create table if not exists item(itemcode varchar(20),itemname varchar(20),Price float)")
    conn.commit()
    cursor.close()
    conn.close()
    print("This was executed")


def insert_value():
    item_code = input("Please enter the item code: ")
    item_name = input("Please enter the item name: ")
    price = int(input("Please enter the price: "))
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute("insert into item (itemcode,itemname,price) values( %s ,%s,%s)", [item_code, item_name, price])
    conn.commit()
    cursor.close()
    conn.close()


def display():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute("select * from item;")
    tasks = cursor.fetchall()
    print(tasks)
    conn.commit()
    cursor.close()
    conn.close()


def search():
    itemcode = input("Please enter the item code")
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute(f"select * from item where itemcode = {itemcode};")
    tasks = cursor.fetchall()
    print(tasks)
    conn.commit()
    cursor.close()
    conn.close()


create_table()
while True:
    print("\n> MAIN MENU")
    print("[1] Add new items.")
    print("[2] View all items.")
    print("[3] Search for a item")
    print("[4] Exit")
    choice2 = int(input("Desired operation: [1/2/3/4] "))
    if choice2 == 1:
        insert_value()
    elif choice2 == 2:
        display()
    elif choice2 == 3:
        search()
    elif choice2 == 4:
        break
    else:
        print("Invalid Choice")

'''
Output:

This was executed

> MAIN MENU
[1] Add new items.
[2] View all items.
[3] Search for a item
[4] Exit
Desired operation: [1/2/3/4] 1
Please enter the item code: 3
Please enter the item name: Cup
Please enter the price: 400

> MAIN MENU
[1] Add new items.
[2] View all items.
[3] Search for a item
[4] Exit
Desired operation: [1/2/3/4] 2
[('1', 'chips', 20.0), ('2', 'Phone', 75000.0), ('3', 'Cup', 400.0)]

> MAIN MENU
[1] Add new items.
[2] View all items.
[3] Search for a item
[4] Exit
Desired operation: [1/2/3/4] 3
Please enter the item code2
[('2', 'Phone', 75000.0)]

> MAIN MENU
[1] Add new items.
[2] View all items.
[3] Search for a item
[4] Exit
Desired operation: [1/2/3/4] 4

Process finished with exit code 0

'''

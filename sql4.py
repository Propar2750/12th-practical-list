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
    cursor.execute(
        "create table if not exists student(rollno int primary key,name varchar(30) not null,Class int,DOB date, Gender varchar(2))")
    conn.commit()
    cursor.close()
    conn.close()
    print("This was executed")


def insert_value():
    rollno = int(input("Please enter the students roll no.: "))
    name = input("Please enter the students name:  ")
    classa = int(input("Please enter the class:  "))
    dob = input("Please enter the date of birth: ")
    Gender = input("Please enter the gender(F/M): ")
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute("insert into student values( %s ,%s,%s,%s,%s)", [rollno, name, classa, dob, Gender])
    conn.commit()
    cursor.close()
    conn.close()


def display():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")  # use database
    cursor.execute("select * from student;")
    tasks = cursor.fetchall()
    print(tasks)
    conn.commit()
    cursor.close()
    conn.close()


def alter():
    print("Welcome to the Student Update Program")
    rollno = int(input("Enter the roll number of the student to update: "))
    field = input("Enter the field you want to update (e.g., name, class, DOB, Gender): ")
    new_value = input(f"Enter the new value for {field}: ")

    # Check if the new value is numeric or not
    if field.lower() in ["class"]:
        new_value = int(new_value)  # Convert to integer for numeric fields
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("use class12projects;")
    try:
        # Ensure the table exists
        cursor.execute(f"SELECT * FROM student WHERE rollno = {rollno};")
        if cursor.fetchone() is None:
            print(f"No student found with roll number {rollno}.")
            return

        # Update the field with the new value
        query = f"UPDATE student SET {field} = %s WHERE rollno = %s;"
        cursor.execute(query, (new_value, rollno))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Updated {field} for roll number {rollno} to {new_value}.")
        else:
            print("No rows were updated. Please check the roll number and try again.")
    except sqltor.Error as e:
        print(f"Error while updating data: {e}")

    conn.commit()
    cursor.close()
    conn.close()


create_table()
while True:
    print("\n> MAIN MENU")
    print("[1] Add new student.")
    print("[2] View all students.")
    print("[3] Alter data of a student.")
    print("[4] Exit")
    choice2 = int(input("Desired operation: [1/2/3/4] "))
    if choice2 == 1:
        insert_value()
    elif choice2 == 2:
        display()
    elif choice2 == 3:
        alter()
    elif choice2 == 4:
        break
    else:
        print("Invalid Choice")

'''
This was executed

> MAIN MENU
[1] Add new student.
[2] View all students.
[3] Alter data of a student.
[4] Exit
Desired operation: [1/2/3/4] 1
Please enter the students roll no.: 2
Please enter the students name:  Tamana 
Please enter the class:  12
Please enter the date of birth: 2007-10-15
Please enter the gender(F/M): F

> MAIN MENU
[1] Add new student.
[2] View all students.
[3] Alter data of a student.
[4] Exit
Desired operation: [1/2/3/4] 2
[(2, 'Tamana ', 12, datetime.date(2007, 10, 15), 'F'), (30111, 'Krishang', 12, datetime.date(2007, 10, 15), 'M')]

> MAIN MENU
[1] Add new student.
[2] View all students.
[3] Alter data of a student.
[4] Exit
Desired operation: [1/2/3/4] 3
Welcome to the Student Update Program
Enter the roll number of the student to update: 2
Enter the field you want to update (e.g., name, class, DOB, Gender): name
Enter the new value for name: Kamana
Updated name for roll number 2 to Kamana.

> MAIN MENU
[1] Add new student.
[2] View all students.
[3] Alter data of a student.
[4] Exit
Desired operation: [1/2/3/4] 2
[(2, 'Kamana', 12, datetime.date(2007, 10, 15), 'F'), (30111, 'Krishang', 12, datetime.date(2007, 10, 15), 'M')]

> MAIN MENU
[1] Add new student.
[2] View all students.
[3] Alter data of a student.
[4] Exit
Desired operation: [1/2/3/4] 4

Process finished with exit code 0

'''

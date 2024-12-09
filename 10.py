import pickle

def write_customers_to_file_input(n, filename="hotel.dat"):
    customers = []
    for i in range(n):
        roomno = input(f"Enter room number for customer {i + 1}: ")
        name = input(f"Enter name for customer {i + 1}: ")
        duration = int(input(f"Enter duration (in days) for customer {i + 1}: "))
        customer = {"roomno": roomno, "name": name, "duration": duration}
        customers.append(customer)
    
    # Open file in append mode to retain previous records
    with open(filename, "ab") as file:
        for customer in customers:
            pickle.dump(customer, file)
    print(f"\n{n} customers added to the file.")
    
# Part (i): Read n dictionary objects and write them into the file
def write_customers_to_file_dictionary(dictionary, filename="hotel.dat"):
    n=len(dictionary.keys())
    print(dictionary.keys())
    customers = []
    for i in range(n):
        
        customer = {"roomno": dictionary[list(dictionary.keys())[i]][0], "name": dictionary[list(dictionary.keys())[i]][1], "duration": dictionary[list(dictionary.keys())[i]][2]}
        customers.append(customer)
    
    # Open file in append mode to retain previous records
    with open(filename, "ab") as file:
        for customer in customers:
            pickle.dump(customer, file)
    print(f"\n{n} customers added to the file.")

# Part (ii): Read all dictionary objects from the file and print them
def read_customers_from_file(filename="hotel.dat"):
    try:
        with open(filename, "rb") as file:
            print("\nAll Customers in the File:")
            while True:
                customer = pickle.load(file)
                print(customer)
    except EOFError:
        pass
    except FileNotFoundError:
        print("File not found. Please add records first.")

# Part (iii): Count the number of customers in the file
def count_customers_in_file(filename="hotel.dat"):
    count = 0
    try:
        with open(filename, "rb") as file:
            while True:
                pickle.load(file)
                count += 1
    except EOFError:
        pass
    except FileNotFoundError:
        print("File not found. Please add records first.")
    print(f"\nTotal number of customers in the hotel: {count}")
    return count

# Part (iv): Display customers who stayed more than 2 days
def display_long_stay_customers(filename="hotel.dat"):
    try:
        with open(filename, "rb") as file:
            print("\nCustomers who stayed more than 2 days:")
            while True:
                customer = pickle.load(file)
                if customer["duration"] > 2:
                    print(customer)
    except EOFError:
        pass
    except FileNotFoundError:
        print("File not found. Please add records first.")

sample_customers = {
    101: (101, "John Doe", 3),
    102: (102, "Jane Smith", 5),
    103: (103, "Alice Brown", 2),
    104: (104, "Bob Johnson", 7)
}
write_customers_to_file_dictionary(sample_customers)

# Example Usage
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Add Customers to File")
        print("2. Display All Customers")
        print("3. Count Total Customers")
        print("4. Display Customers with Stay > 2 Days")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("How many customers do you want to add? "))
            write_customers_to_file(n)
        elif choice == 2:
            read_customers_from_file()
        elif choice == 3:
            count_customers_in_file()
        elif choice == 4:
            display_long_stay_customers()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


'''
Output:

4 customers added to the file.

Menu:
1. Add Customers to File
2. Display All Customers
3. Count Total Customers
4. Display Customers with Stay > 2 Days
5. Exit
Enter your choice: 2

All Customers in the File:
{'roomno': 101, 'name': 'John Doe', 'duration': 3}
{'roomno': 102, 'name': 'Jane Smith', 'duration': 5}
{'roomno': 103, 'name': 'Alice Brown', 'duration': 2}
{'roomno': 104, 'name': 'Bob Johnson', 'duration': 7}

Menu:
1. Add Customers to File
2. Display All Customers
3. Count Total Customers
4. Display Customers with Stay > 2 Days
5. Exit
Enter your choice: 3

Total number of customers in the hotel: 4

Menu:
1. Add Customers to File
2. Display All Customers
3. Count Total Customers
4. Display Customers with Stay > 2 Days
5. Exit
Enter your choice: 4

Customers who stayed more than 2 days:
{'roomno': 101, 'name': 'John Doe', 'duration': 3}
{'roomno': 102, 'name': 'Jane Smith', 'duration': 5}
{'roomno': 104, 'name': 'Bob Johnson', 'duration': 7}

Menu:
1. Add Customers to File
2. Display All Customers
3. Count Total Customers
4. Display Customers with Stay > 2 Days
5. Exit
Enter your choice: 5
Exiting the program.
'''

import pickle

# Part (i): Read n dictionary objects and write them into the file
def write_customers_to_file(n, filename="hotel.dat"):
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
def simulate_ring_game():
    """Simulate the ring game by taking user inputs and arranging rings."""
    stack = []
    temp_stack = []

    while True:
        user_input = input("Enter the diameter of the ring (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break

        try:
            diameter = int(user_input)

            # Compare and manage stacks
            while stack and stack[-1] < diameter:
                temp_stack.append(stack.pop())
                print("Current stack:", stack)

            stack.append(diameter)
            print("Current stack:", stack)

            while temp_stack:
                stack.append(temp_stack.pop())
                print("Current stack:", stack)

        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")


if __name__ == "__main__":
    simulate_ring_game()

'''
Output: 
Enter the diameter of the ring (or type 'done' to finish): 5
Current stack: [5]
Enter the diameter of the ring (or type 'done' to finish): 4
Current stack: [5, 4]
Enter the diameter of the ring (or type 'done' to finish): 3
Current stack: [5, 4, 3]
Enter the diameter of the ring (or type 'done' to finish): 2
Current stack: [5, 4, 3, 2]
Enter the diameter of the ring (or type 'done' to finish): 1
Current stack: [5, 4, 3, 2, 1]
Enter the diameter of the ring (or type 'done' to finish): 4
Current stack: [5, 4, 3, 2]
Current stack: [5, 4, 3]
Current stack: [5, 4]
Current stack: [5, 4, 4]
Current stack: [5, 4, 4, 3]
Current stack: [5, 4, 4, 3, 2]
Current stack: [5, 4, 4, 3, 2, 1]
Enter the diameter of the ring (or type 'done' to finish): 6
Current stack: [5, 4, 4, 3, 2]
Current stack: [5, 4, 4, 3]
Current stack: [5, 4, 4]
Current stack: [5, 4]
Current stack: [5]
Current stack: []
Current stack: [6]
Current stack: [6, 5]
Current stack: [6, 5, 4]
Current stack: [6, 5, 4, 4]
Current stack: [6, 5, 4, 4, 3]
Current stack: [6, 5, 4, 4, 3, 2]
Current stack: [6, 5, 4, 4, 3, 2, 1]
Enter the diameter of the ring (or type 'done' to finish): done

Process finished with exit code 0
'''

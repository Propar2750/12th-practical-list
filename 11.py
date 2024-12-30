import pandas as pd

def read_and_print_file(file_path):
    """Reads the CSV file and prints the data."""
    try:
        data = pd.read_csv(file_path)
        print(data)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def count_total_people(data):
    """Counts the total number of people in the placement test."""
    return len(data)

def find_top_n_students(data, n):
    """Finds the top n names based on total marks using simple lists and loops."""
    # Compute total marks for each student
    total_marks = []
    for i in range(len(data)):
        marks = 0
        for col in data.columns[2:]:  # Skip the 'Name' column
            marks += int(data.iloc[i][col])
        total_marks.append(marks)

    # Find the top n students manually
    top_students = []
    for _ in range(n):
        max_marks = -1
        max_index = -1
        for i in range(len(total_marks)):
            if total_marks[i] > max_marks:
                max_marks = total_marks[i]
                max_index = i
        if max_index != -1:
            top_students.append((data.iloc[max_index]['Name'], max_marks))
            total_marks[max_index] = -1  # Exclude this student from further consideration

    return top_students

# Example usage:
file_path = "placements.csv"
data = read_and_print_file(file_path)
if data is not None:
    # a) Total number of people who came for the placement test
    total_people = count_total_people(data)
    print(f"Total number of people: {total_people}")

    # b) Top n students based on total marks
    n = 3  # Change this value for different top 'n'
    top_students = find_top_n_students(data, n)
    print(f"Top {n} students based on total marks:")
    for name, marks in top_students:
        print(f"{name}: {marks}")

'''
Output:
   SNO      Name  Marks1  Marks2  Marks3  Marks4  Marks5
0    1      John       4       3       4       2       5
1    2     peter       3       4       4       3       5
2    3      Parv       5       5       5       5       5
3    4  Krishang       1       2       3       2       3
Total number of people: 4
Top 3 students based on total marks:
Parv: 25
peter: 19
John: 18
'''

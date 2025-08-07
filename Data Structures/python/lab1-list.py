# Basic List Operations

# Create an empty list
list_of_files = []
print(list_of_files)
# Append elements to the list (adding items to the end)
file1 = "raj.txt"
file2 = "ajeet.txt"
list_of_files.append(file1)
list_of_files.append(file2)
print(list_of_files)
# Access an element by index
print(list_of_files[0])
print(list_of_files[1])
# Modify an element
file3 = "arjun.txt"
list_of_files[0] = file3
print(list_of_files)
# Insert an element at a specific index

# Remove an element by value

# Remove and return an element by index using pop.
# No argument means pop last element.

# Check if an element exists

# Iterate through the list

# Find the length of the list

# Reverse a list

# Sort a list

# Create a new sorted list without modifying the original

# Create a list comprehension (squares of numbers from 1 to 5)

# Basic List Operations

# Create an empty list
my_list = []

# Append elements to the list (adding items to the end)
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)  # Output: [10, 20, 30]

# Access an element by index
print(my_list[1])  # Output: 20

# Modify an element
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30]

# Insert an element at a specific index
my_list.insert(1, 15)
print(my_list)  # Output: [10, 15, 25, 30]

# Remove an element by value
my_list.remove(25)
print(my_list)  # Output: [10, 15, 30]

# Remove and return an element by index using pop.
# No argument means pop last element.
last_element = my_list.pop()
print(last_element)  # Output: 30
print(my_list)  # Output: [10, 15]

# Check if an element exists
if 10 in my_list:
    print("10 is in the list")  # Output: 10 is in the list

# Iterate through the list
for item in my_list:
    print(item)  # Output: 10  15

# Find the length of the list
print(len(my_list))  # Output: 2

# Reverse a list
my_list.reverse()
print(my_list)  # Output: [15, 10]

# Sort a list
numbers = [5, 3, 8, 1, 4]
numbers.sort()
print(numbers)  # Output: [1, 3, 4, 5, 8]

# Create a new sorted list without modifying the original
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [8, 5, 4, 3, 1]
print(numbers)  # Output: [1, 3, 4, 5, 8] (unchanged)

# Create a list comprehension (squares of numbers from 1 to 5)
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

"""
Python Task Manager App
Storing tasks as strings within a list
"""

# Globally available data structure
tasks = [
    "Watch course introduction video",
    "Fork the course GitHub repository to my own GitHub account",
    "Spin up a GitHub CodeSpace for the forked repository",
    "Start working through Chapter 2"
]


# Core Functions
def add_task(task):
    """Add a new task"""
    global tasks
    tasks.append(task)
    print(f"Task added: {task}")


def delete_task(task):
    """Delete a task by its name."""
    global tasks
    if task in tasks:
        tasks.remove(task)
        print(f"Task deleted: {task}")
    else:
        print(f"Task not found: {task}")


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")


# Main Program
if __name__ == "__main__":
    print("Task Manager with Lists")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View All Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            status = input("Enter task status (default: pending): ") or "pending"
            deadline = input("Enter task deadline (optional): ") or None
            add_task(title, status, deadline)
        elif choice == "2":
            title = input("Enter task title to delete: ")
            delete_task(title)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
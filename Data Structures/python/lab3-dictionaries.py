# Basic Dictionary Operations

# Create an empty dictionary

# Add key-value pairs to the dictionary

# Access a value using a key

# Modify an existing value

# Check if a key exists

# Remove a key-value pair using del

# Remove a key-value pair using pop (also returns the value)

# Add more items

# Iterate through dictionary keys

# Iterate through dictionary values

# Iterate through key-value pairs

# Basic Dictionary Operations

# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict["name"] = "Alice"
my_dict["age"] = 25
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Access a value using a key
print(my_dict["name"])  # Output: Alice

# Modify an existing value
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Check if a key exists
if "city" in my_dict:
    print("City:", my_dict["city"])  # Output: City: New York

if "country" not in my_dict:
    print("Key 'country' not found")  # Output: Key 'country' not found

# Remove a key-value pair using del
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}

# Remove a key-value pair using pop (also returns the value)
age = my_dict.pop("age")
print(age)  # Output: 26
print(my_dict)  # Output: {'name': 'Alice'}

# Add more items
my_dict["profession"] = "Engineer"
my_dict["hobby"] = "Painting"

# Iterate through dictionary keys
for key in my_dict:
    print(key, "->", my_dict[key])
# Output:
# name -> Alice
# profession -> Engineer
# hobby -> Painting

# Iterate through dictionary values
for value in my_dict.values():
    print(value)
# Output:
# Alice
# Engineer
# Painting

# Iterate through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# profession: Engineer
# hobby: Painting

"""
Python Task Manager App
Storing task data in dictionaries
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks
    # TODO assign to `task` a dictionary containing key:value pairs for
    # the "title", "status" and "deadline" taken from the function arguments.
    tasks.append(task)
    print(f"Task added: {task}")


def delete_task(title):
    """Delete a task by title."""
    global tasks
    task_to_delete = None
    for task in tasks:
        # TODO Check whether the title of the current task matches the `title` argument
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task deleted: {task_to_delete}")
    else:
        print(f"Task not found: {title}")


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager with Dictionaries")
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


# this is the 

"""
Python Task Manager App
Storing task data in dictionaries
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks
    task = {"title": title, "status": status, "deadline": deadline}
    tasks.append(task)
    print(f"Task added: {task}")


def delete_task(title):
    """Delete a task by title."""
    global tasks
    task_to_delete = None
    for task in tasks:
        if task["title"] == title:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task deleted: {task_to_delete}")
    else:
        print(f"Task not found: {title}")


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager with Dictionaries")
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


"""
Python Task Manager App
Edit Tasks Functionality
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks
    task = {"title": title, "status": status, "deadline": deadline}
    tasks.append(task)
    print(f"Task added: {task}")


def delete_task(title):
    """Delete a task by title."""
    global tasks
    task_to_delete = None
    for task in tasks:
        if task["title"] == title:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task deleted: {task_to_delete}")
    else:
        print(f"Task not found: {title}")


def edit_task(title):
    """Edit a task's details."""
    # TODO allow this function to modify the global variable `tasks`
    task_to_edit = None
    # TODO iterate through `tasks` and if a title match is found,
    # set `task_to_edit` to the current task and then break out of the loop.
    if task_to_edit:
        print(f"Editing task: {task_to_edit}")
        print("\nLeave a property blank to retain its current value.")
        task_to_edit.update({
            "title": input(f"Enter new title (current: {task_to_edit['title']}): ") or task_to_edit["title"],
            # TODO use the same format as for "title" to update "status",
            # including defaulting to the original value,
            "deadline": input(f"Enter new deadline (current: {task_to_edit['deadline']}): ") or task_to_edit[
                "deadline"]
        })
        print(f"Task edited: {task_to_edit}")
    else:
        print(f"Task not found: {title}")


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager with Edit Task Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. View All Tasks")
        print("5. Exit")

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
            title = input("Enter task title to edit: ")
            edit_task(title)
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


"""
Python Task Manager App
Edit Tasks Functionality
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks
    task = {"title": title, "status": status, "deadline": deadline}
    tasks.append(task)
    print(f"Task added: {task}")


def delete_task(title):
    """Delete a task by title."""
    global tasks
    task_to_delete = None
    for task in tasks:
        if task["title"] == title:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task deleted: {task_to_delete}")
    else:
        print(f"Task not found: {title}")


def edit_task(title):
    """Edit a task's details."""
    global tasks
    task_to_edit = None
    for task in tasks:
        if task["title"] == title:
            task_to_edit = task
            break
    if task_to_edit:
        print(f"Editing task: {task_to_edit}")
        print("\nLeave a property blank to retain its current value.")
        task_to_edit.update({
            "title": input(f"Enter new title (current: {task_to_edit['title']}): ") or task_to_edit["title"],
            "status": input(f"Enter new status (current: {task_to_edit['status']}): ") or task_to_edit["status"],
            "deadline": input(f"Enter new deadline (current: {task_to_edit['deadline']}): ") or task_to_edit[
                "deadline"]
        })
        print(f"Task edited: {task_to_edit}")
    else:
        print(f"Task not found: {title}")


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager with Edit Task Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. View All Tasks")
        print("5. Exit")

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
            title = input("Enter task title to edit: ")
            edit_task(title)
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
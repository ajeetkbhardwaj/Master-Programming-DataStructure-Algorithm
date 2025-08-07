# Basic Stack Operations

# Create an empty stack

# Push elements onto the stack

# Pop an element from the stack (removes the last element)

# Peek at the top element without removing it

# Check if the stack is empty

# Use a stack to reverse a list by popping all elements

# Basic Stack Operations

# Create an empty stack
stack = []

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  # Output: [10, 20, 30]

# Pop an element from the stack (removes the last element)
print(stack.pop())  # Output: 30
print(stack)  # Output: [10, 20]

# Peek at the top element without removing it
print(stack[-1])  # Output: 20
print(stack)  # Output: [10, 20] (unchanged)

# Check if the stack is empty
if not stack:  # Equivalent to if len(stack) == 0
    print("Stack is empty")
else:
    print("Stack is not empty")  # Output: Stack is not empty

# Use a stack to reverse a list by popping all elements
stack = [1, 2, 3, 4, 5]
reversed_list = []

while stack: # Equivalent to `while len(stack) > 0`
    reversed_list.append(stack.pop())

print(reversed_list)  # Output: [5, 4, 3, 2, 1]


"""
Python Task Manager App
Adding Undo Last Action Functionality.
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]

# Stack to hold undo actions
undo_stack = []


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks, undo_stack
    task = {"title": title, "status": status, "deadline": deadline}
    tasks.append(task)
    undo_stack.append(("delete", task.copy()))  # If we want to undo this, we'll delete the task.
    print(f"Task added: {task}")


def delete_task(title):
    """Delete a task by title."""
    global tasks, undo_stack
    task_to_delete = None
    for task in tasks:
        if task["title"] == title:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        undo_stack.append(("add", task_to_delete.copy()))  # If we want to undo this, we'll add the task back
        print(f"Task deleted: {task_to_delete}")
    else:
        print(f"Task not found: {title}")


def edit_task(title):
    """Edit a task's details."""
    global tasks, undo_stack
    task_to_edit = None
    for task in tasks:
        if task["title"] == title:
            task_to_edit = task
            break
    if task_to_edit:
        # Create a copy of the original task for undo
        original_task = task_to_edit.copy()

        print(f"Editing task: {task_to_edit}")
        print("\nLeave a property blank to retain its current value.")
        task_to_edit.update({
            "title": input(f"Enter new title (current: {task_to_edit['title']}): ") or task_to_edit["title"],
            "status": input(f"Enter new status (current: {task_to_edit['status']}): ") or task_to_edit["status"],
            "deadline": input(f"Enter new deadline (current: {task_to_edit['deadline']}): ") or task_to_edit[
                "deadline"]
        })

        # Push the original task to undo stack before editing
        undo_stack.append(("edit", original_task, task_to_edit.copy()))
        print(f"Task edited: {task_to_edit}")
    else:
        print(f"Task not found: {title}")


def undo_last_action():
    """Undo the last action."""
    global tasks
    if not undo_stack:
        print("No actions to undo.")
        return

    action_data = undo_stack.pop()

    if action_data[0] == "delete":
        task = action_data[1]
        if task in tasks:
            tasks.remove(task)
            print(f"Addition undone: {task}")
        else:
            print("Task not found in list when trying to delete.")

    elif action_data[0] == "add":
        task = action_data[1]
        if task not in tasks:
            tasks.append(task)
            print(f"Undid delete: {task}")
        else:
            print("Task already in list when trying to add.")

    elif action_data[0] == "edit":
        original_task = action_data[1]
        edited_task = action_data[2]
        for i, task in enumerate(tasks):
            if task["title"] == edited_task["title"]:
                tasks[i] = original_task  # Restore original task
                print(f"Undid edit: Restored task to {original_task}")
                break


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
    print("Task Manager with Undo Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Undo Last Action")
        print("5. View All Tasks")
        print("6. Exit")

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
            undo_last_action()
        elif choice == "5":
            view_tasks()
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


"""
Python Task Manager App
Adding Undo Last Action Functionality.
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]

# Stack to hold undo actions
undo_stack = []


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks, undo_stack
    task = {"title": title, "status": status, "deadline": deadline}
    tasks.append(task)
    undo_stack.append(("delete", task.copy()))  # If we want to undo this, we'll delete the task.
    print(f"Task added: {task}")


def delete_task(title):
    """Delete a task by title."""
    global tasks, undo_stack
    task_to_delete = None
    for task in tasks:
        if task["title"] == title:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        undo_stack.append(("add", task_to_delete.copy()))  # If we want to undo this, we'll add the task back
        print(f"Task deleted: {task_to_delete}")
    else:
        print(f"Task not found: {title}")


def edit_task(title):
    """Edit a task's details."""
    global tasks, undo_stack
    task_to_edit = None
    for task in tasks:
        if task["title"] == title:
            task_to_edit = task
            break
    if task_to_edit:
        # Create a copy of the original task for undo
        original_task = task_to_edit.copy()

        print(f"Editing task: {task_to_edit}")
        print("\nLeave a property blank to retain its current value.")
        task_to_edit.update({
            "title": input(f"Enter new title (current: {task_to_edit['title']}): ") or task_to_edit["title"],
            "status": input(f"Enter new status (current: {task_to_edit['status']}): ") or task_to_edit["status"],
            "deadline": input(f"Enter new deadline (current: {task_to_edit['deadline']}): ") or task_to_edit[
                "deadline"]
        })

        # Push the original task to undo stack before editing
        undo_stack.append(("edit", original_task, task_to_edit.copy()))
        print(f"Task edited: {task_to_edit}")
    else:
        print(f"Task not found: {title}")


def undo_last_action():
    """Undo the last action."""
    global tasks
    if not undo_stack:
        print("No actions to undo.")
        return

    action_data = undo_stack.pop()

    if action_data[0] == "delete":
        task = action_data[1]
        if task in tasks:
            tasks.remove(task)
            print(f"Addition undone: {task}")
        else:
            print("Task not found in list when trying to delete.")

    elif action_data[0] == "add":
        task = action_data[1]
        if task not in tasks:
            tasks.append(task)
            print(f"Undid delete: {task}")
        else:
            print("Task already in list when trying to add.")

    elif action_data[0] == "edit":
        original_task = action_data[1]
        edited_task = action_data[2]
        for i, task in enumerate(tasks):
            if task["title"] == edited_task["title"]:
                tasks[i] = original_task  # Restore original task
                print(f"Undid edit: Restored task to {original_task}")
                break


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
    print("Task Manager with Undo Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Undo Last Action")
        print("5. View All Tasks")
        print("6. Exit")

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
            undo_last_action()
        elif choice == "5":
            view_tasks()
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


"""
Python Task Manager App
Adding Undo Last Action Functionality.
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]

# Stack to hold undo actions
undo_stack = []


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks, undo_stack
    task = {"title": title, "status": status, "deadline": deadline}
    tasks.append(task)
    undo_stack.append(("delete", task.copy()))  # If we want to undo this, we'll delete the task.
    print(f"Task added: {task}")
    print(f"Undo stack state: {undo_stack}")  # Print undo stack after update


def delete_task(title):
    """Delete a task by title."""
    global tasks, undo_stack
    task_to_delete = None
    for task in tasks:
        if task["title"] == title:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        undo_stack.append(("add", task_to_delete.copy()))  # If we want to undo this, we'll add the task back
        print(f"Task deleted: {task_to_delete}")
        print(f"Undo stack state: {undo_stack}")  # Print undo stack after update
    else:
        print(f"Task not found: {title}")


def edit_task(title):
    """Edit a task's details."""
    global tasks, undo_stack
    task_to_edit = None
    for task in tasks:
        if task["title"] == title:
            task_to_edit = task
            break
    if task_to_edit:
        # Create a copy of the original task for undo
        original_task = task_to_edit.copy()

        print(f"Editing task: {task_to_edit}")
        print("\nLeave a property blank to retain its current value.")
        task_to_edit.update({
            "title": input(f"Enter new title (current: {task_to_edit['title']}): ") or task_to_edit["title"],
            "status": input(f"Enter new status (current: {task_to_edit['status']}): ") or task_to_edit["status"],
            "deadline": input(f"Enter new deadline (current: {task_to_edit['deadline']}): ") or task_to_edit[
                "deadline"]
        })

        # Push the original task to undo stack before editing
        undo_stack.append(("edit", original_task, task_to_edit.copy()))
        print(f"Task edited: {task_to_edit}")
        print(f"Undo stack state: {undo_stack}")  # Print undo stack after update
    else:
        print(f"Task not found: {title}")


def undo_last_action():
    """Undo the last action."""
    global tasks
    if not undo_stack:
        print("No actions to undo.")
        return

    action_data = undo_stack.pop()
    print(f"Undoing action: {action_data}")
    print(f"Undo stack state after pop: {undo_stack}")  # Print undo stack after pop

    if action_data[0] == "delete":
        task = action_data[1]
        if task in tasks:
            tasks.remove(task)
            print(f"Addition undone: {task}")
        else:
            print("Task not found in list when trying to delete.")

    elif action_data[0] == "add":
        task = action_data[1]
        if task not in tasks:
            tasks.append(task)
            print(f"Undid delete: {task}")
        else:
            print("Task already in list when trying to add.")

    elif action_data[0] == "edit":
        original_task = action_data[1]
        edited_task = action_data[2]
        for i, task in enumerate(tasks):
            if task["title"] == edited_task["title"]:
                tasks[i] = original_task  # Restore original task
                print(f"Undid edit: Restored task to {original_task}")
                break


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
    print("Task Manager with Undo Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Undo Last Action")
        print("5. View All Tasks")
        print("6. Exit")

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
            undo_last_action()
        elif choice == "5":
            view_tasks()
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
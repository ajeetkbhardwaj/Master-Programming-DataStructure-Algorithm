# Basic JSON Operations

# Import the json module

# Load JSON data from a file

# Print the loaded JSON data

# Access and print specific values

# Modify the JSON data (update age, add a new skill)

# Print updated data

# Save the modified data back to the JSON file

# Verify changes by reloading the JSON file

 # Check output  reflects the updated JSON content

# Basic JSON Operations

# Import the json module
import json

# Load JSON data from a file
with open("data.json", "r") as file:
    data = json.load(file)

# Print the loaded JSON data
print(data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'skills': ['Python', 'SQL', 'Machine Learning']}

# Access and print specific values
print(data["name"])  # Output: Alice
print(data["skills"])  # Output: ['Python', 'SQL', 'Machine Learning']

# Modify the JSON data (update age, add a new skill)
data["age"] = 26
data["skills"].append("Data Analysis")

# Print updated data
print(
    data)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'skills': ['Python', 'SQL', 'Machine Learning', 'Data Analysis']}

# Save the modified data back to the JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Verify changes by reloading the JSON file
with open("data.json", "r") as file:
    updated_data = json.load(file)

print(updated_data)  # Output should reflect the updated JSON content

"""
Python Task Manager App
Adding functionality to save tasks to an external json file.
"""

import heapq
import json

# Globally available data structures
tasks = []
priority_queue = []
undo_stack = []

# Core Functions
def rebuild_priority_queue():
    """Rebuild the priority queue from the current task list."""
    global priority_queue
    priority_queue = [(task["priority"], idx, task) for idx, task in enumerate(tasks)]
    heapq.heapify(priority_queue)


def load_tasks_from_json(filename):
    """Load tasks from a JSON file."""
    global tasks, undo_stack
    try:
        with open(filename, "r") as file:
            # TODO Load the contents of `file` into the global variable `tasks`.

        # TODO rebuild the priority queue
        undo_stack.clear()  # Clear undo stack on reload
        print(f"Tasks successfully loaded from {filename}.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")


def add_task(title, status="pending", deadline=None, priority=2):
    """Add a new task with status, deadline, and priority."""
    global tasks, undo_stack
    task = {"title": title, "status": status, "deadline": deadline, "priority": priority}
    tasks.append(task)
    heapq.heappush(priority_queue, (priority, len(tasks) - 1, task))
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
        rebuild_priority_queue()
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
                "deadline"],
            "priority": int(
                input(f"Enter new priority (current: {task_to_edit['priority']}): ") or task_to_edit["priority"])
        })

        # Push the original task to undo stack before editing
        undo_stack.append(("edit", original_task, task_to_edit.copy()))
        rebuild_priority_queue()
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
            rebuild_priority_queue()  # Rebuild to remove task from priority_queue
            print(f"Addition undone: {task}")
        else:
            print("Task not found in list when trying to delete.")

    elif action_data[0] == "add":
        task = action_data[1]
        if task not in tasks:
            tasks.append(task)
            rebuild_priority_queue()  # Rebuild to re-add the task properly
            print(f"Undid delete: {task}")
        else:
            print("Task already in list when trying to add.")

    elif action_data[0] == "edit":
        original_task = action_data[1]
        edited_task = action_data[2]
        for i, task in enumerate(tasks):
            if task["title"] == edited_task["title"]:
                tasks[i] = original_task  # Restore original task
                rebuild_priority_queue()
                print(f"Undid edit: Restored task to {original_task}")
                break


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']}, Priority: {task['priority']})")


def view_priority_tasks():
    """View tasks sorted by priority without altering the original queue."""
    print("\nTasks by Priority:")
    heap_copy = priority_queue[:]
    while heap_copy:
        priority, idx, task = heapq.heappop(heap_copy)
        print(f"Priority {priority}: {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager: With Load Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Undo Last Action")
        print("5. View All Tasks")
        print("6. View Tasks by Priority")
        print("7. Load Tasks from JSON")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            status = input("Enter task status (default: pending): ") or "pending"
            deadline = input("Enter task deadline (optional): ") or None
            priority = int(input("Enter task priority (default: 2): ") or 2)
            add_task(title, status, deadline, priority)
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
            view_priority_tasks()
        elif choice == "7":
            filename = input("Enter the filename to load tasks from: ")
            load_tasks_from_json(filename)
        elif choice == "8":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


"""
Python Task Manager App
Adding functionality to save tasks to an external json file.
"""

import heapq
import json

# Globally available data structures
tasks = []
priority_queue = []
undo_stack = []


# Core Functions
def rebuild_priority_queue():
    """Rebuild the priority queue from the current task list."""
    global priority_queue
    priority_queue = [(task["priority"], idx, task) for idx, task in enumerate(tasks)]
    heapq.heapify(priority_queue)


def load_tasks_from_json(filename):
    """Load tasks from a JSON file."""
    global tasks, undo_stack
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        rebuild_priority_queue()
        undo_stack.clear()  # Clear undo stack on reload
        print(f"Tasks successfully loaded from {filename}.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")


def add_task(title, status="pending", deadline=None, priority=2):
    """Add a new task with status, deadline, and priority."""
    global tasks, undo_stack
    task = {"title": title, "status": status, "deadline": deadline, "priority": priority}
    tasks.append(task)
    heapq.heappush(priority_queue, (priority, len(tasks) - 1, task))
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
        rebuild_priority_queue()
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
                "deadline"],
            "priority": int(
                input(f"Enter new priority (current: {task_to_edit['priority']}): ") or task_to_edit["priority"])
        })

        # Push the original task to undo stack before editing
        undo_stack.append(("edit", original_task, task_to_edit.copy()))
        rebuild_priority_queue()
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
            rebuild_priority_queue()  # Rebuild to remove task from priority_queue
            print(f"Addition undone: {task}")
        else:
            print("Task not found in list when trying to delete.")

    elif action_data[0] == "add":
        task = action_data[1]
        if task not in tasks:
            tasks.append(task)
            rebuild_priority_queue()  # Rebuild to re-add the task properly
            print(f"Undid delete: {task}")
        else:
            print("Task already in list when trying to add.")

    elif action_data[0] == "edit":
        original_task = action_data[1]
        edited_task = action_data[2]
        for i, task in enumerate(tasks):
            if task["title"] == edited_task["title"]:
                tasks[i] = original_task  # Restore original task
                rebuild_priority_queue()
                print(f"Undid edit: Restored task to {original_task}")
                break


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']}, Priority: {task['priority']})")


def view_priority_tasks():
    """View tasks sorted by priority without altering the original queue."""
    print("\nTasks by Priority:")
    heap_copy = priority_queue[:]
    while heap_copy:
        priority, idx, task = heapq.heappop(heap_copy)
        print(f"Priority {priority}: {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager: With Load Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Undo Last Action")
        print("5. View All Tasks")
        print("6. View Tasks by Priority")
        print("7. Load Tasks from JSON")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            status = input("Enter task status (default: pending): ") or "pending"
            deadline = input("Enter task deadline (optional): ") or None
            priority = int(input("Enter task priority (default: 2): ") or 2)
            add_task(title, status, deadline, priority)
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
            view_priority_tasks()
        elif choice == "7":
            filename = input("Enter the filename to load tasks from: ")
            load_tasks_from_json(filename)
        elif choice == "8":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


"""
Python Task Manager App
Adding functionality to save tasks to an external json file.
"""

import heapq
import json

# Globally available data structures
tasks = []
priority_queue = []
undo_stack = []


# Core Functions
def rebuild_priority_queue():
    """Rebuild the priority queue from the current task list."""
    global priority_queue
    priority_queue = [(task["priority"], idx, task) for idx, task in enumerate(tasks)]
    heapq.heapify(priority_queue)


def load_tasks_from_json(filename):
    """Load tasks from a JSON file."""
    global tasks, undo_stack
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        rebuild_priority_queue()
        undo_stack.clear()  # Clear undo stack on reload
        print(f"Tasks successfully loaded from {filename}.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")


def save_tasks_to_json(filename):
    """Save tasks to a JSON file."""
    try:
        with open(filename, "w") as file:
            # TODO use json.dump() to write `tasks` to `filename` with an indent of 4 spaces.
        print(f"Tasks successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def add_task(title, status="pending", deadline=None, priority=2):
    """Add a new task with status, deadline, and priority."""
    global tasks, undo_stack
    task = {"title": title, "status": status, "deadline": deadline, "priority": priority}
    tasks.append(task)
    heapq.heappush(priority_queue, (priority, len(tasks) - 1, task))
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
        rebuild_priority_queue()
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
                "deadline"],
            "priority": int(
                input(f"Enter new priority (current: {task_to_edit['priority']}): ") or task_to_edit["priority"])
        })

        # Push the original task to undo stack before editing
        undo_stack.append(("edit", original_task, task_to_edit.copy()))
        rebuild_priority_queue()
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
            rebuild_priority_queue()  # Rebuild to remove task from priority_queue
            print(f"Addition undone: {task}")
        else:
            print("Task not found in list when trying to delete.")

    elif action_data[0] == "add":
        task = action_data[1]
        if task not in tasks:
            tasks.append(task)
            rebuild_priority_queue()  # Rebuild to re-add the task properly
            print(f"Undid delete: {task}")
        else:
            print("Task already in list when trying to add.")

    elif action_data[0] == "edit":
        original_task = action_data[1]
        edited_task = action_data[2]
        for i, task in enumerate(tasks):
            if task["title"] == edited_task["title"]:
                tasks[i] = original_task  # Restore original task
                rebuild_priority_queue()
                print(f"Undid edit: Restored task to {original_task}")
                break


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']}, Priority: {task['priority']})")


def view_priority_tasks():
    """View tasks sorted by priority without altering the original queue."""
    print("\nTasks by Priority:")
    heap_copy = priority_queue[:]
    while heap_copy:
        priority, idx, task = heapq.heappop(heap_copy)
        print(f"Priority {priority}: {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager: With Save and Load Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Undo Last Action")
        print("5. View All Tasks")
        print("6. View Tasks by Priority")
        print("7. Load Tasks from JSON")
        print("8. Save Tasks to JSON")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            status = input("Enter task status (default: pending): ") or "pending"
            deadline = input("Enter task deadline (optional): ") or None
            priority = int(input("Enter task priority (default: 2): ") or 2)
            add_task(title, status, deadline, priority)
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
            view_priority_tasks()
        elif choice == "7":
            filename = input("Enter the filename to load tasks from: ")
            load_tasks_from_json(filename)
        elif choice == "8":
            filename = input("Enter the filename to save tasks to: ")
            save_tasks_to_json(filename)
        elif choice == "9":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

"""
Python Task Manager App
Adding functionality to save tasks to an external json file.
"""

import heapq
import json

# Globally available data structures
tasks = []
priority_queue = []
undo_stack = []


# Core Functions
def rebuild_priority_queue():
    """Rebuild the priority queue from the current task list."""
    global priority_queue
    priority_queue = [(task["priority"], idx, task) for idx, task in enumerate(tasks)]
    heapq.heapify(priority_queue)


def load_tasks_from_json(filename):
    """Load tasks from a JSON file."""
    global tasks, undo_stack
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        rebuild_priority_queue()
        undo_stack.clear()  # Clear undo stack on reload
        print(f"Tasks successfully loaded from {filename}.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")


def save_tasks_to_json(filename):
    """Save tasks to a JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"Tasks successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def add_task(title, status="pending", deadline=None, priority=2):
    """Add a new task with status, deadline, and priority."""
    global tasks, undo_stack
    task = {"title": title, "status": status, "deadline": deadline, "priority": priority}
    tasks.append(task)
    heapq.heappush(priority_queue, (priority, len(tasks) - 1, task))
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
        rebuild_priority_queue()
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
                "deadline"],
            "priority": int(
                input(f"Enter new priority (current: {task_to_edit['priority']}): ") or task_to_edit["priority"])
        })

        # Push the original task to undo stack before editing
        undo_stack.append(("edit", original_task, task_to_edit.copy()))
        rebuild_priority_queue()
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
            rebuild_priority_queue()  # Rebuild to remove task from priority_queue
            print(f"Addition undone: {task}")
        else:
            print("Task not found in list when trying to delete.")

    elif action_data[0] == "add":
        task = action_data[1]
        if task not in tasks:
            tasks.append(task)
            rebuild_priority_queue()  # Rebuild to re-add the task properly
            print(f"Undid delete: {task}")
        else:
            print("Task already in list when trying to add.")

    elif action_data[0] == "edit":
        original_task = action_data[1]
        edited_task = action_data[2]
        for i, task in enumerate(tasks):
            if task["title"] == edited_task["title"]:
                tasks[i] = original_task  # Restore original task
                rebuild_priority_queue()
                print(f"Undid edit: Restored task to {original_task}")
                break


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']}, Priority: {task['priority']})")


def view_priority_tasks():
    """View tasks sorted by priority without altering the original queue."""
    print("\nTasks by Priority:")
    heap_copy = priority_queue[:]
    while heap_copy:
        priority, idx, task = heapq.heappop(heap_copy)
        print(f"Priority {priority}: {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager: With Save and Load Functionality")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Undo Last Action")
        print("5. View All Tasks")
        print("6. View Tasks by Priority")
        print("7. Load Tasks from JSON")
        print("8. Save Tasks to JSON")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            status = input("Enter task status (default: pending): ") or "pending"
            deadline = input("Enter task deadline (optional): ") or None
            priority = int(input("Enter task priority (default: 2): ") or 2)
            add_task(title, status, deadline, priority)
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
            view_priority_tasks()
        elif choice == "7":
            filename = input("Enter the filename to load tasks from: ")
            load_tasks_from_json(filename)
        elif choice == "8":
            filename = input("Enter the filename to save tasks to: ")
            save_tasks_to_json(filename)
        elif choice == "9":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, name):
        self.name = name

# Create objects
university = University("Example University")
department = Department("Computer Science")
course = Course("Introduction to Programming")

# Compose objects
university.add_department(department)
department.add_course(course)

# Access composed objects
print(university.name)  # Output: Example University
print(department.name)  # Output: Computer Science
print(course.name)      # Output: Introduction to Programming
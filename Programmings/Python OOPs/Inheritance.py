# Define a parent class
class Animal:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print("Generic sound")

# Define a child class that inherits from Animal
class Cat(Animal):
    def __init__(self, name, whiskers):
        super().__init__(name)  # Call parent class constructor
        self.whiskers = whiskers

    def sound(self):
        print("Meow!")  # Override parent class method

# Create an object from the child class
my_cat = Cat("Whiskers", 5)

# Access object attributes and methods
print(my_cat.name)    # Output: Whiskers
print(my_cat.whiskers)  # Output: 5
my_cat.sound()       # Output: Meow!
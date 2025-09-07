# Define a class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Create an object from the class
my_dog = Dog("Fido", 3)
# Access object attributes and methods
print(my_dog.name)  # Output: Fido
print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Woof!
"""
Abstraction is the practice of showing only the necessary information to the outside world while hiding the internal details. 
In Python, abstraction can be achieved through abstract classes and interfaces.
"""
from abc import ABC, abstractmethod

# Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

# Define concrete classes that inherit from Vehicle
class Car(Vehicle):
    def start_engine(self):
        print("Vroom!")

    def accelerate(self):
        print("Speeding up...")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Revving...")

    def accelerate(self):
        print("Zooming...")

# Create objects from the concrete classes
car = Car()
motorcycle = Motorcycle()

# Call abstract methods
car.start_engine()  # Output: Vroom!
car.accelerate()    # Output: Speeding up...
motorcycle.start_engine()  # Output: Revving...
motorcycle.accelerate()    # Output: Zooming...
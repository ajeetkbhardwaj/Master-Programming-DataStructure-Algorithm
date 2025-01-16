"""
lab-0.py

We start the our first programming lab in python which act as introduction
to programming language class, where we learn to practice about
1. How to write, execute a program on python interpreter or ide ?
2. How to display output on the user screen ?
3. learn about different data types that exits in python like
3.1 Integer
3.2 Float(decimal)
3.3 Boolean
3.4 String(text)
3.5 Complex
3.6 List
3.7 Tuple
3.8 Sets
3.9 Dictionary
4. What are variables and how to declare them in python ?
5. What are keywords and how to use them in python ?
6. what are identifiers and how to use them in python ?
7. What are operators and how to use them in python ?
"""

#%% 1. How to write, execute a program in python ?
print("Hello, World !")

#%% 2. How to display output on the user screen ?
print("Ajeet Kumar")
print('Ajeet Kumar')
print('''Ajeet Kumar''')
# print(Ajeet Kumar) # Error: NameError: name 'Ajeet' is not defined
print(121)
print(3.14)
print(True)
print(False)
print(3+4j)
print("heelo", 121, 3.14, True, False, 3+4j)
print("heelo", 121, 3.14, True, False, 3+4j, sep=",")
print("heelo", 121, 3.14, True, False, 3+4j, sep="--")
print("Ajeet", end="-")
print("Kumar")

#%% 3. learn about different data types that exits in python

# single line comment
"""

In Python, there are several built-in data types that we can use to store different types of data. 
Here are some examples:

1. Integer: Whole numbers, e.g., 1, 2, 3
2. Float: Decimal numbers, e.g., 1.1, 2.2, 3.3
3. Boolean: True or False values
4. String: Text, e.g., "Hello, World!"
5. Complex: Complex numbers, e.g., 3+4j
6. List: Ordered collection of items, e.g., [1, 2, 3]
7. Tuple: Ordered, immutable collection of items, e.g., (1, 2, 3)
8. Set: Unordered collection of unique items, e.g., {1, 2, 3}
9. Dictionary: Collection of key-value pairs, e.g., {"name": "Ajeet", "age": 30}
"""
print(1923)
print(2.34)
print(True)
print(False)
print(type(1923))
print(type(2.34))
print(type(True))
print(type(False))
# print(true) # Error: NameError: name 'true' is not defined because python is case sensitive
print("Ajeet Kumar")
print(type("Ajeet Kumar"))
print(3+4j)
print(type(3+4j))
print([1, 2, 3, 4, 5])
print(type([1, 2, 3, 4, 5]))
print((1, 2, 3, 4, 5))
print(type((1, 2, 3, 4, 5)))
print({1, 2, 3, 4, 5})
print(type({1, 2, 3, 4, 5}))
print({"name": "Ajeet", "age": 22, "gender": "male", "height": 1.})
print(type({"name": "Ajeet", "age": 22, "gender": "male"}))

#%% . Convert inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54

inches = 5.7
cm = inches_to_cm(inches)
print(f"{inches} inch = {cm} cm")

#  Convert foot to centimeters
def foot_to_cm(feet):
    return feet * 30.48

feet = 5.6
cm = foot_to_cm(feet)
print(f"{feet} feet = {cm} cm")
# %% 5. What are variables and how to declare them in python ?
a = 10
print(a)
b = 4.3
print(b)
c = False
print(c)
name = "Ajeet Kumar"
print("Welcome", name)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# Dynamic typing
a = 7 #integer
# static typing
#int a = 7 # c, c++, java

# Dynamic Binding
a = 8
print(a)
a = "Ajeet"
print(a)
# Static Binding
#int a = 8
#str a = "Ajeet"
#print(a)

a = 1
b = 2
c = 3

print(a,b,c)

a,b,c = 1,2,3
print(a,b,c)

a = 5
b = 5
c = 5

print(a,b,c)

a=b=c = 5
print(a,b,c)

# %%
import keyword
print(keyword.kwlist)

print(keyword.iskeyword('if'))
print(keyword.iskeyword('else'))
"""
# async, await: Used for defining asynchronous functions and awaiting their results.
import asyncio

async def main():
    await asyncio.sleep(1)
    return "Hello"

result = asyncio.run(main())
print(result)           # Output after one second delay: Hello 
"""
#%% 
# Scope and Name space keywords
# nonlocal: Refers to variables in the nearest enclosing scope that is not global.
def outer():
    x = "local"

    def inner():
        nonlocal x     # Refers to the variable x in outer()
        x = "nonlocal"
        print(x)

    inner()
    print(x)

outer()                 # Output: nonlocal \n nonlocal 
# global: Declares a variable as global.
count = 0

def increment():
    global count        # Refers to the global variable count
    count += 1

increment()
print(count)           # Output: 1

# Context management keywords
# with: Used to wrap the execution of a block with methods defined by a context manager.
with open('file.txt', 'w') as f:
    f.write('Hello World!') 

# as: Used to create an alias for a module or import a module with an alias.
import math as m

print(m.sqrt(16))      # Output: 4.0

try:
    x = int("invalid")
except ValueError as e:
    print(e)            # Output: invalid literal for int() with base ...

# function and class keywords
# def: Used to define a function or method.
def greet(name):
    return f"Hello {name}!"

print(greet("Alice"))   # Output: Hello Alice!

# return: Exits a function and optionally returns a value.
def absolute_value(x):
    if x >= 0:
        return x
    else:
        return -x
res = absolute_value(-5)
print(res)              # Output: 5
def add(x, y):
    return x + y

result = add(5, 3)
print(result)           # Output: 8

# lambda: Creates an anonymous function.
double = lambda x: x * 2
print(double)
print(double(5))        # Output: 10

# class: Used to define a class.
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"
my_dog = Dog("Buddy")
print(my_dog.name)      # Output: Buddy
print(my_dog.bark())    # Output: Woof!

# control flow keywords
# pass: Used as a placeholder where no action is required.
def placeholder():
    pass
for i in range(10):
    if i > 5:
        break
    else:
        pass

#break, continue : Used to alter the flow of a loop.
for i in range(10):
    if i == 3:
        break
    print(i)
# Output: 0 1 2

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9

# if, elif, else: Used for conditional execution.
x = 10
if x < 5:
    print("Less than five")
elif x == 10:
    print("Equal to ten")   # Output: Equal to ten
else:
    print("Greater than five")

# for, while : Used for looping.
for i in range(5):
    print(i)              # Output: 0, 1, 2, 3, 4

count = 0
while count < 5:
    print(count)         # Output: 0, 1, 2, 3, 4
    count += 1

# operator keywords
# and, or, not: Used for logical operations.
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False

# in, not in: Used to check for membership.
print('x' in ['x', 'y', 'z'])     # Output: True
print('a' not in ['x', 'y', 'z']) # Output: True

# is, is not: Used for identity testing.
x = [1, 2, 3]
print(x is x)          # Output: True
print(x is not x)      # Output: False

# value keywords
# True, False, None: Used to represent truth values and absence of value.
print(True)            # Output: True
print(False)           # Output: False
print(None)            # Output: None

# assert : Used for debugging purposes.
x = 4
assert x < 5, "Invalid value"

# del: Used to delete objects.
x = 10
del x
#print(x)

# import, from, as: Used to import modules or specific objects from modules.
import math
print(math.sqrt(16))   # Output: 4.0
from math import sqrt
import time
import calendar
import datetime
print(sqrt(16))        # Output: 4.0

# except, raise, try: Used for exception handling.
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)            # Output: division by zero

# finally: Used to execute code upon termination of a block, regardless of an exception.
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)            # Output: division by zero
finally:
    print("This code will run no matter what")

# %% 6. what are identifiers and how to use them in python ?
name = "Ajeet Kumar"
a = 23
1name = "Ajeet Kumar" # Error: SyntaxError: invalid syntax
name1 = "Ajeet Kumar"
*name = "Ajeet Kumar" # Error: SyntaxError: starred assignment target must be in a list or tuple
name* = "Ajeet Kumar" # Error: SyntaxError: can't assign to operator
_name = "Ajeet Kumar"
name_ = "Ajeet Kumar"
_name_ = "Ajeet Kumar"
name@ = "Ajeet Kumar" # Error: SyntaxError: invalid syntax
@name = "Ajeet Kumar" # Error: SyntaxError: invalid syntax

# %% 7. What are operators and how to use them in python ?

# Arithmetic Operators
a = 10
b = 3
print(a + b)    # Output: 13
print(a - b)    # Output: 7
print(a * b)    # Output: 30
print(a / b)    # Output: 3.3333333333333335
print(a % b)    # Output: 1

print(a ** b) # Output: 1000

#comparision operator
a = 10
b = 3
print(a > b) # Output: True
print(a < b) # Output: False
print(a == b) # Output: False
print(a != b) # Output: True
print(a >= b) # Output: True
print(a <= b) # Output: False

#Logical Operator
a = 10
b = 3
c = 5
print(a > b and b > c) # Output: False
print(a > b or b > c) # Output: True
print(not(a > b)) # Output: False

#assignment operator
a = 10
b = 3

a += b # same as a = a + b
print(a) # Output: 13

a -= b # same as a = a - b
print(a) # Output: 10

a *= b # same as a = a * b
print(a) # Output: 30

a /= b # same as a = a / b
print(a) # Output: 10.0

a %= b # same as a = a % b
print(a) # Output: 1.0

a **= b # same as a = a ** b
print(a) # Output: 1.0


#bitwise operator
a = 10 # binary 1010
b = 3 # binary 0011
#changes to check git


print(a & b) # Output: 2 (binary 0010)
print(a | b) # Output: 11 (binary 1011)
print(a ^ b) # Output: 9 (binary 1001)
print(~a) # Output: -11
print(a << 2) # Output: 40 (binary 101000)
print(a >> 2) # Output: 2 (binary 0010)

#%%
# static - Calender, Clock
# dynamic - Timer, Stopwatch
# Static - Calendar
def print_calendar(year, month):
    print(calendar.month(year, month))

print_calendar(2023, 10)

# Static - Clock
def print_current_time():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

print_current_time()

# Dynamic - Timer
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print('Timer completed!')

countdown_timer(10)

# Dynamic - Stopwatch
def stopwatch():
    print("Press Enter to start the stopwatch")
    input()
    start_time = time.time()
    print("Stopwatch started. Press Enter to stop.")
    input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

stopwatch()

#%% 
number = input("Enter a number: ")
print(number)
print(type(number))
decimal = float(number)
print(decimal)
print(type(decimal))
integer = int(decimal)
print(integer)
print(type(integer))
string = input("Enter a string: ")
var = string
print(var)
print(type(var))
print(string)
# string = int(string) # Error: ValueError: invalid literal for int() with base 10: 'Ajeet'
# string = float(string) # Error: ValueError: could not convert string to float: 'Ajeet'
# string = bool(string) # Error: ValueError: invalid literal for int() with base 10: 'Ajeet'
# string = complex(string) # Error: ValueError: complex() arg is a malformed string
com = complex(decimal) 
print(com)

#%% Arithmetic calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the Second number: "))

results = num1 + num2

print(results)
#%%
""" 
References and Citations
1. Python Documentation: https://docs.python.org/3/
2. Real Python Tutorials: https://realpython.com/
3. W3Schools Python Tutorial: https://www.w3schools.com/python/
4. Python Programming.net: https://pythonprogramming.net/
5. Programiz Python Tutorial: https://www.programiz.com/python-programming
6. Python for Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/
7. Python Crash Course: https://nostarch.com/pythoncrashcourse
8. Python Cookbook: https://www.oreilly.com/library/view/python-cookbook/0596001673/
9. Python Tricks: https://realpython.com/products/python-tricks-book/
10. Python Practice Book: https://anandology.com/python-practice-book/index.html
11. Python Programming: https://www.geeksforgeeks.org/python-programming-language/
12. Python Programming: https://www.tutorialspoint.com/python/index.htm
13. Python Programming: https://www.javatpoint.com/python-tutorial
14. Python Programming: https://www.learnpython.org/
15. Python Programming: https://www.programiz.com/python-programming
16. Python Programming: https://www.nptel.ac.in/courses/106/106/106106182/
17. Python Programming: https://www.codecademy.com/learn/learn-python
18. Python Programming: https://www.sololearn.com/Course/Python/
19. Python Programming: https://www.coursera.org/specializations/python
20. Python Programming: https://www.edx.org/learn/python
"""
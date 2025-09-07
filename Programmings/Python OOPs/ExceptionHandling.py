try:
    # Code that might raise an exception
    x = 1 / 0
except ZeroDivisionError as e:
    # Handle the exception
    print("Caught an exception:", e)
finally:
    # Code that runs regardless of exceptions
    print("Finally block executed")

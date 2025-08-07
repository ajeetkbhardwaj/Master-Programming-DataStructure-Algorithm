"""
1. How to handle the utility directory path when importing classes or function to the our run-script ? : making the utils path as sys path then call from there.

"""
import sys
import os
import time

Dirpath = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(Dirpath)
print(project)
utilsPath = os.path.join(project, 'lab1')
print(utilsPath)
if utilsPath not in sys.path:
    sys.path.insert(0, utilsPath)
    print("yes")
# Now you can import the util module from the common directory
from lab1.hello import hello_asynch, greet, test
print(greet("Ajeet"))  # Output: Hello, Ajeet!

"""
aysnch func()
The async keyword in Python is used to declare a function as a “coroutine.” A coroutine is a special kind of function that can be paused and resumed, allowing Python to handle other tasks in the meantime.
await func()
The await keyword is used inside an async function to call another async function and wait for it to finish. The function being called with await is also a coroutine.

we use the await keyword to call asyncio.sleep(1), which is a coroutine that pauses execution for one second. After the pause, we print ‘Hello, World!’.

The power of async and await shown where multiple coroutines and I/O-bound tasks
"""
import asyncio
asyncio.run(hello_asynch())

"""
# Async for I/O-bound Tasks - operations that spend most of their time waiting for input/output operations to complete, such as reading from or writing to a file, making network requests, or querying a database.

When an I/O-bound task is executed in a traditional synchronous manner, the entire program waits for the task to complete before moving onto the next task.

 With async, however, the program can move on to other tasks while waiting for the I/O-bound task to complete.
 
 """

start = time.time()
asyncio.run(test())
asyncio.run(test())
end = time.time()
print(start)
print(end)
print(end - start)

"""
Managing Multiple Async Tasks : 

Async in Python also allows us to manage multiple tasks at once. This is achieved using the asyncio.gather() function, which runs multiple coroutines concurrently and waits for all of them to finish.

"""

async def main(): # Define a top-level async function
    print("Main program started")
    await asyncio.gather(test(), test()) # Await the gather call
    print("Main program finished")



"""
For the concurrent task
Threading in Python can be used to run multiple tasks concurrently. 
However, due to Python’s Global Interpreter Lock (GIL), threads in Python are not truly concurrent and 
may not provide a significant speedup for CPU-bound tasks.


"""
import threading
import time
start = time.time()
thread1 = threading.Thread(target=test)
thread2 = threading.Thread(target=test)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()

print(f'Total time: {end - start}')


"""

Multiprocessing in Python allows for the creation of separate processes, each with its own Python interpreter and memory space, thus bypassing the GIL and allowing for true parallelism.

multiprocessing module to create two processes that run the test() function in parallel. The total time taken is approximately 1 second, similar to using asyncio.gather() and threading.
While threading and multiprocessing provide alternatives to async, they come with their own trade-offs. Threading does not provide true concurrency due to the GIL, and multiprocessing involves more overhead due to the creation of separate processes. Therefore, the choice between async, threading, and multiprocessing will depend on the specific requirements of your task.

"""
import time
import multiprocessing

start = time.time()
process1 = multiprocessing.Process(target=test)
process2 = multiprocessing.Process(target=test)
process1.start()
process2.start()
process1.join()
process2.join()
end = time.time()

print(f"The total time: {end - start}")

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main()) # Run the top-level async function
    end = time.time()
    print(f"the time difference: {end - start}")
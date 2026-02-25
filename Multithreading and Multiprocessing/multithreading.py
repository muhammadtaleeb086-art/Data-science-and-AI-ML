## Multithreading in Python
## when to use multithreading in python
## 1. I/O-bound tasks: If your program spends a lot of time waiting for input/output operations (like reading/writing files, making network requests, or interacting with databases), multithreading can help improve performance by allowing other threads to run while one thread is waiting.
## Concurrent execution: If you want to perform multiple tasks concurrently (like handling multiple user requests in a web server), multithreading can help you achieve that without blocking the main thread.


import threading
import time

def print_numbers():
  for i in range(5):
    time.sleep(2)  # Simulating a time-consuming task
    print(f"Number : {i}")

def print_letters():
  for letter in 'ABCDE':
    time.sleep(2)  # Simulating a time-consuming task
    print(f"Letter : {letter}")

## Create 2 threads for the functions
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)


t=time.time()
## Start the threads
thread1.start()
thread2.start()

## Wait for both threads to finish
thread1.join()
thread2.join()

finish=time.time() - t
print(f"Time taken with threading: {finish} seconds") 
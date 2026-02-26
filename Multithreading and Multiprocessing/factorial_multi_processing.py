"""
Real-world Example : Multiprocessing for CPU-bound tasks
Scenario : Factorial Calculation
Factorial Calculation , especially for large numbers,involve siginificant computational work. Multiprocessing can be used to speed up the calculation by distributing the workload across multiple CPU cores.
"""

import multiprocessing
import math
import time
import sys

#Increase the maximum number of digits for interger conversion
sys.set_int_max_str_digits(100000)

#Function to compute  calculate factorial of a number
def compute_factorial(number):
  print(f"Computing factorial of {number}")
  result = math.factorial(number)
  print(f"Factorial of {number} is {result}")
  return result


if __name__ == "__main__":
  numbers = [5000, 6000, 700, 8000] #List of numbers to compute factorial for

  start_time = time.time()

  #Create a pool of processes equal to the number of CPU cores
  with multiprocessing.Pool() as pool:
    results = pool.map(compute_factorial, numbers)

  end_time = time.time()
  print(f"Total time taken: {end_time - start_time} seconds")

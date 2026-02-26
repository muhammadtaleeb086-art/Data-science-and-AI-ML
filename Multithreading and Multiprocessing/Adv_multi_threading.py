## Multithreading with thread Pool Executor
from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
  time.sleep(1)
  return f"Number: {number}"

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with ThreadPoolExecutor(max_workers=3) as executor:
  results = list(executor.map(print_number, number))

for result in results:
  print(result)
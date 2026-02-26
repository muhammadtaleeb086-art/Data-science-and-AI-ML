## Processes that run in parallel 
## CPU-Bound Tasks - Tasks that are heavy on CPU usage (e.g:Mathematical computations,Data processing).
## Paralle Execution - Multiple Cores of the CPU

import multiprocessing
import time

def square_number():
  for i in range(5):
    time.sleep(1)
    print(f'Square of {i} : {i*i}')

def cube_number():
  for i in range(5):
    time.sleep(1.5)
    print(f'Cube of {i} : {i*i*i}')

if __name__ == '__main__':

  ## Create 2 processes for the functions
  process1 = multiprocessing.Process(target=square_number)
  process2 = multiprocessing.Process(target=cube_number)


  ## Start the processes 
  t=time.time()
  process1.start()
  process2.start()

  ## Wait for both processes to finish
  process1.join()
  process2.join()
  print(f"Total time taken: {time.time() - t}")
### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square of {number}: {number ** 2}"

def main():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square_number, numbers))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
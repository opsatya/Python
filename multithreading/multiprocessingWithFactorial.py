import multiprocessing
import time
import sys
import math


sys.set_int_max_str_digits(100000)


def FindFactorials(num):
    print(f'computing factorial of {num}')
    res = math.factorial(num)
    return res


if __name__ == '__main__':
    numbers = [1200,1433,232]

    strTime = time.time()

    with multiprocessing.Pool() as pool:
        result = pool.map(FindFactorials,numbers)
    
    endTime = time.time()

    print(f'Results: {result}')
    print(f'time taken: {endTime-strTime}seconds')
    
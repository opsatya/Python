### multithreading using the thread pool excuter

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f'numbers : {number}'

numbers = [1,2,44,5,3,5,3,5,43]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)

for result in results:
    print(result)

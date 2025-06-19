from concurrent.futures import ProcessPoolExecutor
import time
def PrintSquare(number):
    time.sleep(2)
    return number*number

number = [12,3,412,12]

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executer:
        results = executer.map(PrintSquare,number)
    for res in results:
        print(res)

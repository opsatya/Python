import threading
import time
def printTable(num):
    time.sleep(2)
    for i in range(1,num+1):
        print(num*i)


def reverseStr(str):  
    time.sleep(1)
    print(str[::-1])

t = time.time()

t1 = threading.Thread(target=printTable,args=(5,))
t2 = threading.Thread(target=reverseStr, args=('satya',))


print('hello world')

t1.start()
t2.start()

t1.join()
t2.join()

total_exec = time.time() - t
print(total_exec)
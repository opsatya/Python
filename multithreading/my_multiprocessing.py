# process that run parallaly
# cpu bound task - task that are heavey on CPU usages (e.g mathamatical, computations,etc)
# parallel excution - multiple cores of the cpu


# | Feature                        | **Multithreading** 🧵                 | **Multiprocessing** 🔥                         |
# | ------------------------------ | ------------------------------------- | ---------------------------------------------- |
# | **Runs on**                    | Single CPU core (mostly)              | Multiple CPU cores                             |
# | **Best for**                   | I/O-bound tasks (e.g. file, network)  | CPU-bound tasks (e.g. math, ML, heavy loops)   |
# | **Python GIL**                 | YES – one thread runs at a time       | NO – each process is a full Python interpreter |
# | **Memory shared?**             | Yes – threads share memory            | No – each process has its own memory           |
# | **Overhead**                   | Low                                   | Higher (due to process creation, memory)       |
# | **Communication between them** | Easy (shared variables)               | Harder (needs `Queue`, `Pipe`, etc.)           |
# | **Crash behavior**             | Crash in one thread can affect others | Processes are isolated (more robust)           |


import multiprocessing
import time

def squareNumber():
    time.sleep(2)
    for i in range(5):
        print(i*i)

def cubeNumber():
    time.sleep(2.5)
    for i in range(5):
        print(i*i*i)

p1 = multiprocessing.Process(target = squareNumber)
p2 = multiprocessing.Process(target = cubeNumber)

t = time.time()
p1.start()
p2.start()

p1.join()
p2.join()

finish_task = time.time() - t
print(finish_task)
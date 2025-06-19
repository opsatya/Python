
---

Programs, processes, and threads form the foundation of modern computing. A **program** is a static set of instructions, while a **process** is its dynamic execution instance. **Threads** enable concurrent task execution within a process. Let's explore these concepts in detail:

## Program
A program is a static executable file containing instructions written in a programming language (e.g., Chrome's `.exe` file) [1][2]. Key characteristics:
- Resides on storage until executed
- Can spawn multiple processes (e.g., opening multiple Chrome windows)
- Examples: Microsoft Word, Excel, browser executables

## Process
A process is a program in execution with dedicated resources [3][4]:
- **Memory segments**:
  - **Text**: Executable code
  - **Data**: Global variables
  - **Heap**: Dynamically allocated memory
  - **Stack**: Function calls/local variables [3]
- **Process Control Block (PCB)** stores:
  - Process state (new, ready, running, waiting, terminated) [3]
  - Program counter and CPU registers
  - Memory allocation details
  - I/O status information [3]

**Process lifecycle**:
```
New → Ready ↔ Running → Waiting → Terminated
```
Processes are isolated - one process cannot directly access another's memory [2][4]. Example: Each Chrome tab runs as a separate process [1].

## Thread
A thread is the smallest execution unit within a process [1][2]:
- Shares process memory (code, data, heap)
- Has private stack and registers
- Types:
  - **Single-threaded**: One execution flow (early applications)
  - **Multi-threaded**: Concurrent execution (modern apps)

**Real-world examples**:
- Web browser (Chrome):
  - Main thread: UI rendering
  - Background threads: Network requests, JavaScript execution [4]
- Microsoft Word:
  - Thread 1: User input
  - Thread 2: Spell checking [1]

## Process vs Thread Comparison
| Feature               | Process                          | Thread                          |
|-----------------------|----------------------------------|---------------------------------|
| Memory                | Separate address space          | Shares process memory           |
| Creation Cost         | High (OS resources)              | Low (uses existing resources)    |
| Communication         | Complex (IPC required)           | Simple (shared memory)           |
| Fault Tolerance       | Crash isolated to process        | Thread crash affects all threads |
| Context Switch Speed  | Slow                             | Fast                             |
| Example Use Case      | Independent applications         | Parallel tasks in single app     |

## Multithreading Concepts
**Advantages**:
- Improved responsiveness (UI remains active during background tasks)
- Better resource utilization
- Simplified modeling of concurrent operations [6][2]

**Common Interview Questions**:
1. **Q**: How does `start()` differ from `run()` in Java threads?  
   **A**: `start()` creates a new thread, while `run()` executes in the current thread [7].

2. **Q**: Why are threads called lightweight?  
   **A**: They share process resources, reducing creation overhead [4][1].

3. **Q**: What is a PCB?  
   **A**: Process Control Block stores process state and execution context [3].

**Synchronization Challenges**:
- Race conditions
- Deadlocks
- Thread starvation
- Solved using locks, semaphores, and monitors [5][6]

---

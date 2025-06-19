Great! Here's the content formatted as **digital/printable flashcards** — ideal for quick revision. Each card has a **Question (Front)** and **Answer (Back)**. You can use this with apps like Anki, Quizlet, or print them out.

---

### 🃏 **Flashcard Set: Program, Process, and Thread**

---

**Flashcard 1**
**Q: What is a program?**
**A:** A program is a static file with code stored on disk. It doesn’t run until executed (e.g., `chrome.exe`).

---

**Flashcard 2**
**Q: What is a process?**
**A:** A process is a running instance of a program with its own memory and system resources.

---

**Flashcard 3**
**Q: What is a thread?**
**A:** A thread is the smallest unit of execution inside a process. Multiple threads can run in the same process.

---

**Flashcard 4**
**Q: What parts of memory does a process use?**
**A:**

* Text: Code
* Data: Global/static variables
* Heap: Dynamic memory
* Stack: Local variables/function calls

---

**Flashcard 5**
**Q: What is a Process Control Block (PCB)?**
**A:** It's a data structure that stores process details like state, program counter, memory info, and CPU registers.

---

**Flashcard 6**
**Q: What is the process lifecycle?**
**A:**
`New → Ready ↔ Running → Waiting → Terminated`

---

**Flashcard 7**
**Q: Which parts of memory are shared among threads?**
**A:** Code, data, and heap are shared. Stack and registers are private.

---

**Flashcard 8**
**Q: Example of threads in Chrome?**
**A:**

* Main thread: UI
* Background threads: Download files, run JavaScript

---

**Flashcard 9**
**Q: Example of threads in Microsoft Word?**
**A:**

* Thread 1: Handles typing
* Thread 2: Runs spell check

---

**Flashcard 10**
**Q: Why are threads called lightweight?**
**A:** Because they share process resources, making them faster and easier to create than processes.

---

**Flashcard 11**
**Q: Difference between `start()` and `run()` in Java threads?**
**A:**

* `start()`: Creates a new thread
* `run()`: Runs code in the current thread (no new thread)

---

**Flashcard 12**
**Q: Process vs Thread – key memory difference?**
**A:** Processes have separate memory; threads share memory within the same process.

---

**Flashcard 13**
**Q: Process vs Thread – crash handling?**
**A:**

* Process crash: Others unaffected
* Thread crash: Affects all threads in the same process

---

**Flashcard 14**
**Q: Advantages of multithreading?**
**A:**

* Better responsiveness
* Efficient CPU use
* Simpler modeling of parallel tasks

---

**Flashcard 15**
**Q: Common thread issues?**
**A:**

* Race condition
* Deadlock
* Starvation

---

**Flashcard 16**
**Q: Solutions to synchronization problems?**
**A:**

* Locks (e.g., `synchronized`)
* Semaphores
* Monitors

---

**Flashcard 17**
**Q: Real-life analogy for Program, Process, and Thread?**
**A:**

* Program = Recipe
* Process = Chef using the recipe
* Thread = Workers doing tasks in the kitchen

---

Would you like this exported as a **CSV for Quizlet/Anki**, or a **PDF printable flashcard sheet**?

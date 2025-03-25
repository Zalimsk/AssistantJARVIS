import threading
import time
from clap import main_clap_exe

# Function 1 - Yeh pehla kaam karega
def task1():
    for i in range(5):
        main_clap_exe()
        print(f"Task 1 - Step {i+1}")
        time.sleep(1)

# Function 2 - Yeh dusra kaam karega
def task2():
    for i in range(5):
        print(f"Task 2 - Step {i+1}")
        time.sleep(1.5)

# Function 3 - Yeh teesra kaam karega
def task3():
    for i in range(5):
        print(f"Task 3 - Step {i+1}")
        time.sleep(2)

# Threads banaye ja rahe hain
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread3 = threading.Thread(target=task3)

# Saare threads start kar rahe hain
thread1.start()
thread2.start()
thread3.start()

# Threads ka wait karna jab tak wo complete na ho
thread1.join()
thread2.join()
thread3.join()

print("Saare tasks complete ho gaye!")
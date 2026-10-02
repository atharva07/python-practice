import threading
import time

def task(name):
    print(f"Starting: {name}")
    time.sleep(2)
    print(f"Ending: {name}")

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))
t3 = threading.Thread(target=task, args=("Thread-3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

''' 
When multithreading works well 
1. I/O bound tasks

When multithreading Fails 
1. CPU Bound tasks

How to achieve trure Parallelism
1. Use Multiprocessing
'''
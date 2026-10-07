# Synchronous Example:
# Task A: Make a tea - takes 3 seconds
# Task B: Make a coffee - takes 3 seconds
# So in synchronous: you will first make the Tea, wait until its finished, then make a coffee
# Start -> Make tea (3 sec) -> Make Coffee (3 sec) -> Done 
# Total = 6 seconds

import time

def task(name):
    print(f"{name} started")
    time.sleep(3)
    print(f"{name} finished")

task("Task A")
task("Task B")
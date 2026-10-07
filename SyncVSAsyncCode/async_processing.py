# Asynchronous Example:
# # Task A: Make a tea - takes 3 seconds
# Task B: Make a coffee - takes 3 seconds
# In Asynchronous Processing: You start making tea, and while you're waiting for it, you start making coffee
# Start -> Start Tea, Start Coffee -> Both Done (Total = 3 seconds)
# Async means, while I am waiting for one operation to finish, I can allow other work ot proceed.

# The Critical part is await -> 'I can't make progress right now. I am waiting for I/O. Let another coroutine run'
import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(3)
    print(f"{name} finished")

async def main():
    await asyncio.gather(
        task("Task A"),
        task("Task B")
    )

asyncio.run(main())

# Threading and Asynchronous Processing
# With Threading
# Thread 1 ----- Task A -------
# Thread 2 ----- Task B -------
# Thread 3 ----- Task C -------

# With Asynchronous
# Thread 1 ------ Task A, Task B, Task C
# The eventloop decides which coroutine gets to run

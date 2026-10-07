import time
import asyncio

# this is a synchronous code example, here task 2 will not start until the task 1 is finished
# def task(name):
#     print(f"{name}: started")
#     time.sleep(2)
#     print(f"{name}: finished")

# task("Task 1")
# task("Task 2")

# # This is an Async code example, here task 2 will start while task 1 is still running
# async def task(name):
#     print(f"{name}: started")
#     await asyncio.sleep(2)
#     print(f"{name}: finished")

# async def main():
#     task1 = asyncio.create_task(task("Task 1"))
#     task2 = asyncio.create_task(task("Task 2"))

#     await task1
#     await task2

# asyncio.run(main())    

# async def runOperations():
#     num = 10
#     total = 0
#     for i in range(num):
#         total += num * num

#     print(f"Total: {total}")

# async def executeTasks():
#     task1 = asyncio.create_task(runOperations())
#     task2 = asyncio.create_task(runOperations())

#     await task1
#     await task2

# asyncio.run(executeTasks())

# async def task(name):
#     print(f"{name} started")
#     await asyncio.sleep(3)
#     print(f"{name} finished")

# async def main1():
#     await task("Task 1")
#     await task("Task 2")

# asyncio.run(main1())

# Example of running tasks concurrently
# async def main2():
#     await asyncio.gather(
#         task("Task 1"),
#         task("Task 2")
#     )

# asyncio.run(main2())

async def task(name):
    print(f"{name} started")

result = task("Task 1")
print(result)

asyncio.run(task("Task 1"))
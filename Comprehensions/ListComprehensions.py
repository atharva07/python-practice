squares = [x**x for x in range(4)]
print(squares)

con_sqr = [x**x for x in range(10) if x % 2 == 0]
print(con_sqr) 

list_compr1 = [x for x in range(10) if x % 2 == 0]
print(list_compr1) 

nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens)

squared = [x**2 for x in nums]
print(squared) 

nums = [1, 2, 3, 4, 5, 6]
result = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(result)

logs = [
    "INFO: Service started",
    "ERROR: DB connection failed",
    "WARNING: Disk space low",
    "ERROR: Timeout occurred"
]

errors = [log for log in logs if "ERROR" in log]
print(errors)

users = [
    {"id": 1, "name": "Atharva"},
    {"id": 2, "name": "John"},
    {"id": 3, "name": "Alice"}
]

usernames = [user["name"] for user in users]
print(usernames)

responses = [
    {"status": 200, "data": "ok"},
    {"status": 500, "data": "error"},
    {"status": 404, "data": "not found"}
]

failed_res = [res for res in responses if res["status"] != 200]
print(failed_res)
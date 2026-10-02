square_dict = {x**x for x in range(4)}
print(square_dict)

square_dict_con = {x**x for x in range(10) if x % 2 == 0}
print(square_dict_con)

data = {"a": 5, "b": 15, "c": 20}
result = {key: value for key, value in data.items() if value > 10}
print(result)

data1 = {"a": 1, "b": 2, "c": 3}
swap = {value: key for key, value in data1.items()}
print(swap)

marks = {"math": 80, "eng": 40, "sci": 60}
result = {key: "Pass" if value >= 50 else "Fail" for key, value in marks.items()}
print(result)

users = {
    "u1": {"age": 22},
    "u2": {"age": 30},
    "u3": {"age": 28}
}

result = {key: value for key, value in users.items() if value["age"] > 25}
print(result)

response = [
    {"id": 1, "name": "Atharva"},
    {"id": 2, "name": "John"}
]

result = {item["id"]: item["name"] for item in response}
print(response)

logs = [
    "INFO start",
    "ERROR failed",
    "WARNING low",
    "ERROR timeout"
]

error_log = {i: log for i, log in enumerate(logs) if "ERROR" in log}
print(error_log)

users = {
    "u1": {"age": 22},
    "u2": {"age": 30},
    "u3": {"age": 28}
}

update_user = users["u1"].update({"age": 35})

for key, value in users.items():
    print(f"{key} : {value}")

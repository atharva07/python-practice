a = 4
b = 5

# lambda argument: expression
add = lambda a, b : a + b
print(add(a,b))

students = [("Atharva", 25), ("Darren", 24), ("Neha", 26)]
sorted_students = sorted(students, key = lambda x: x[1])
print(sorted_students)

response = [
    {"name": "Atharva", "age": 25},
    {"name": "Rahul", "age": 21} 
]

print(sorted(response, key = lambda x: x["age"]))

# Sort List of dictionary by salary
employees = [
    {"name": "Atharva", "salary": 50000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Neha", "salary": 60000}
]

sorted_emp = sorted(employees, key = lambda x: x["salary"])
print(sorted_emp)

# Sort List of dictionary by salary in descending order
sorted_emp_desc = sorted(employees, key = lambda x: x["salary"], reverse=True)
sorted_emp_desc1 = sorted(employees, key = lambda x: -x["salary"])

print(sorted_emp_desc)
print(sorted_emp_desc1)

# Get only failed test cases
test_results = [
    {"test_name": "test_login", "status": "passed"},
    {"test_name": "test_add_to_cart", "status": "failed"},
    {"test_name": "test_payment", "status": "failed"}
]

failed_tc = list(filter(lambda x: x["status"] == "failed", test_results))
print(failed_tc)

failed_tc_names = list(filter(lambda x: x["status"] == "failed", test_results))
print(failed_tc_names)

# Convert list of strings → uppercase using map + lambda
browsers = ["chrome", "firefox", "edge"]

upper_case = list(map(lambda x: x.upper(), browsers))
print(upper_case)

lower_case = list(map(lambda x: x.lower(), browsers))
print(lower_case)

first_word_upper = list(map(lambda x: x[0].upper() + x[1:], browsers))
print(first_word_upper)
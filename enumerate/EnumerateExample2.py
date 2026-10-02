items = ['a', 'b', 'c']

for i, item in enumerate(items):
    print(i, item)

marks = [45, 82, 67, 90]

for i, mark in enumerate(marks, start=1):
    if mark >= 50:
        print(f"Student {i}: pass")
    else:
        print(f"Student {i}: Fail")

# Compare Two lists
expected = ["Home", "About", "Contact"]
actual = ["Home", "About", "Services"]

for i, (exp, act) in enumerate(zip(expected, actual)):
    if exp != act:
        print(f"Mismatch at index {i}: expected: {exp} and actual: {act}")


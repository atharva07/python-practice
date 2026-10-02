try:
    num = int("100")
except ValueError:
    print("Invalid number")
else:
    print("Conversation Successful:", num)
finally:
    print("Execution Completed")

# Example 2

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File Found successfully")
finally:
    print("Execution completed")
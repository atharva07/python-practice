def count_up_to(n):
    for i in range(1, n+1):
        yield i

def count_upto_t(n):
    for i in range(1, n+1):
        yield i

count = count_upto_t(10)
print(next(count))

count = count_up_to(10)
print(next(count))
print(next(count))

def count_to_n(n):
    for i in range(1, n+1):
        yield i

count = count_to_n(10)

print(next(count))
print(next(count))
print(next(count))

print("----------- LOG Parsing -------------")

def read_logs(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                yield line

for error in read_logs("File_Handling/file.txt"):
    print(error)

def read_logs(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                yield line

for error in read_logs("File_Handling/file.txt"):
    print(error)
# with open("File_Handling/file.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("File_Handling/file.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("File_Handling/file.txt", "r") as f:
#     for line in f:
#         if "ERROR" in line:
#             print(line.strip())

# with open("File_Handling/file.txt", "r") as f:
#     count = 0
#     for line in f:
#         if "ERROR" in line:
#             count += 1

# print(count)

print("------------ JSON Parsing ------------------")
with open("File_Handling/logs.json", "r") as f:
    for line in f:
        print(line.strip())


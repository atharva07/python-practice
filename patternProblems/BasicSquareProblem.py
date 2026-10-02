# Basic Square Problem
n = 4

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Right Angled Triangle
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

print("Pyramid Pattern")

# Pyramid Pattern
rows = 5
k = 0
for i in range(1, rows+1):
    # Space
    for j in range(1, (rows-i)+1):
        print(end="  ")
    
    # Stars
    while k != (2*i-1):
        print("* ", end="")
        k += 1
    
    k = 0
    print()
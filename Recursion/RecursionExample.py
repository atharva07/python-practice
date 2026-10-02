# def recursive_function(problem):
#     if base_case:
#         return answer
    
#     smaller_problem = reduce(problem)
#     return recursive_function(smaller_problem)

# It like calling a function itself to solve a smaller version of the same problem

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

def print_numbers(n):
    if n == 0:
        return
    
    print(n)
    print_numbers(n-1)

def reverse_string(s):
    if len(s) == 0:
        return ""
    
    print(s[0])
    return reverse_string(s[1:] + s[0])
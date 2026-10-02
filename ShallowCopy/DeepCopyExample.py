# Deep copy creates a new object AND recursively copies all nested objects
# Shallow copy copies reference of nested objects, while deep copy creates completely independent copies of all objects
# so when we do deep copy, so the original one remains the same. 
import copy

original = [[1,2], [3,4]]
deep = copy.deepcopy(original)

deep[0][0] = 99

print(original)
print(deep)
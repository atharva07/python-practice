# Shallow copy creates a new object, but does NOT copy nested objects.
# Instead, it copies reference of inner objects
# Outer Object - new copy
# Inner Object - same (shared)
# So when we do shallow copy, the original copy also changes when we change the element of nested array
import copy

original = [[1,2], [3,4]]
shallow = copy.copy(original)

shallow[0][0] = 99
print(original)
print(shallow)
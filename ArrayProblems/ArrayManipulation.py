list1 = [1,2,3,4,5]
res = []

for i in range(len(list1)-1, -1, -1):
    res.append(list1[i])

print(res)

# How to tell if the list is in ascending order
def is_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

# How to tell if the list in in ascending order, if not can you return the elements that are not in ascending order
def is_ascending_with_elements(lst):
    not_ascending_elements = []
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            not_ascending_elements.append(lst[i])
    if not_ascending_elements:
        return False, not_ascending_elements
    return True, []

list2 = [4,1,3,4,2]
print(is_ascending_with_elements(list2))

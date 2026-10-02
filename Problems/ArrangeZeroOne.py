def sortBinaryArray(arr):
    zero_count = arr.count(0)
    one_count = len(arr) - zero_count
    return [0] * zero_count + [1] * one_count

arr = [0,0,1,0,1,1,1,0]
print(sortBinaryArray(arr))

# Two pointer Approach
def sort_binary(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]

    return arr

arr = [0,0,1,0,1,1,1,0]
print(sort_binary(arr))
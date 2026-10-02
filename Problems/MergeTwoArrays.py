def mergeTwoArrays(nums1, nums2):
    res = []

    for num in nums1:
        res.append(num)

    for num in nums2:
        res.append(num)

    return res

arr1 = [5, 3, 2]
arr2 = [9, 0, 1]
print(mergeTwoArrays(arr1, arr2))
def secondLargestDigitInString(string):
    nums = []

    for char in string:
        if char.isdigit():
            nums.append(int(char))

    largest = nums[0]
    slargest = -1

    for i in range(len(nums)):
        if nums[i] > largest:
            slargest = largest
            largest = nums[i]
        elif nums[i] < largest and nums[i] > slargest:
            slargest = nums[i]

    return slargest

def secondSmallestDigitInString(string):
    nums = []

    for char in string:
        if char.isdigit():
            nums.append(int(char))
    
    sorted_num = sorted(nums, reverse=True)
    print(sorted_num)
    
    return sorted_num[-2]

print(secondSmallestDigitInString("claude240315edualc"))

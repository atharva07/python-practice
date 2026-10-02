def reverseStringKeepSameSpace(string):
    result = list(string)
    left = 0
    right = len(string) - 1

    while left < right:
        if result[left] == ' ':
            left += 1
        elif result[right] == ' ':
            right -= 1
        else:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

    return ''.join(result)

print(reverseStringKeepSameSpace("I am boy"))
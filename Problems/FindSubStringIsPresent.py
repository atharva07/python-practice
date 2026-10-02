def FindSubStringIsPresent(input1, input2):
    if input2 in input1:
        return True
    
    return False

input1 = "programming"
input2 = "gram"
print(FindSubStringIsPresent(input1, input2))
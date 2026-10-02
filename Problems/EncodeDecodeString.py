def encodeDecodeString(string):
    # string = 3[a2[c]]
    stack = []
    current_string = ""
    num = 0

    for ch in string:
        if ch.isdigit():
            num = num * 10 + int(ch)

        elif ch == '[':
            stack.append((current_string, num))
            current_string = ""
            num = 0

        elif ch == ']':
            prev, count = stack.pop()
            current_string = prev + current_string * count

        else:
            current_string += ch

    return current_string

print(encodeDecodeString("3[a2[c]]"))
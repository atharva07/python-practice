string = "aattharvasbb"

def first_unique_char(string):
    freq = {}

    for ch in string:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(string):
        if freq[ch] == 1:
            return i
    
    return -1

print(first_unique_char(string))

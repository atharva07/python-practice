def countWordOccurancesInString(string):
    freq = {}
    words = string.split(" ")

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    for key, value in freq.items():
        print(key,"->",value)

    return freq

print(countWordOccurancesInString("my name is Claude Claude"))
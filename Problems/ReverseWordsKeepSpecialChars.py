import re
def reverse_word_keep_special_chars(s):
    tokens = re.split(r'([^A-Za-z0-9]+)', s)
    print(tokens)

    words = [token for token in tokens if token and token.isalnum()]

    words.reverse()
    print(words)

    result = []
    word_index = 0

    for token in tokens:
        if token and token.isalnum():
            result.append(words[word_index])
            word_index += 1
        else:
            result.append(token)

    return ''.join(result)

s = "hello@world#python"
print(reverse_word_keep_special_chars(s))
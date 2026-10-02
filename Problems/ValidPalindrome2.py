def is_valid_palindrome(string):
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_valid_palindrome("tab a cat"))
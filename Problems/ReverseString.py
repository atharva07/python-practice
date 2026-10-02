class ReverseString:

    def reverseString(self, string: str) -> str:
        chars = list(string)
        left = 0
        right = len(string) - 1

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return ''.join(chars)
    
def main():
    solver = ReverseString()
    string = "Hello"
    result = solver.reverseString(string)
    print(result)

if __name__ == "__main__":
    main()
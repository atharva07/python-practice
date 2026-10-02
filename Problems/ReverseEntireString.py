class ReverseEntireString:
    def reverse_string(self, string: str) -> str:
        char = list(string)
        left = 0
        right = len(string) - 1

        while left < right:
            char[left], char[right] = char[right], char[left]
            left += 1
            right -= 1

        return ''.join(char)
    
def main():
    solver = ReverseEntireString()
    string = "Senior QA Engineer"
    result = solver.reverse_string(string)
    print(result)

if __name__ == "__main__":
    main()

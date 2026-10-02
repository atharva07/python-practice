class IsPalindrome:
    def checkPalindrome(self, string: str) -> bool:
        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True
    
def main():
    solver = IsPalindrome()
    string = "madam"
    result = solver.checkPalindrome(string)
    print(result)

if __name__ == "__main__":
    main()
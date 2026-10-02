class LongestPalindrome:
    def findLongestPalindrome(self, string: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
            return string[left+1:right]
        
        result = ""

        for i in range(len(string)):
            odd = expand(i, i)
            even = expand(i, i+1)

            result = max(result, odd, even, key=len)
        
        return result
        
def main():
    sol = LongestPalindrome()
    res = sol.findLongestPalindrome("babad")
    print(res)

if __name__ == "__main__":
    main()

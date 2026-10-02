class FindFirstNonRepeatingCharacter:
    def firstNonRepeatingChaaracter(self, string: str) -> str:
        freq = {}

        for char in string:
            freq[char] = freq.get(char, 0) + 1

        for key, value in freq.items():
            if value == 1:
                return key

        return ""
    
def main():
    string = "aabbcde"
    res = FindFirstNonRepeatingCharacter()
    result = res.firstNonRepeatingChaaracter(string)
    print(result)

if __name__ == "__main__":
    main()
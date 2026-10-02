class StringCompression:
    def compressString(self, string: str) -> str:
        freq = {}

        for char in string:
            freq[char] = freq.get(char, 0) + 1
        result = []

        for key, value in freq.items():
            result.append(key + str(value))
        return ''.join(result)
    
def main():
    string = "aabcccccaaa"
    solver = StringCompression()
    result = solver.compressString(string)
    print(result)

if __name__ == "__main__":
    main()
class CountOfDuplicateElementInString:
    def countDuplicateElement(self, string: str) -> int:
        freq = {}

        for ch in string:
            freq[ch] = freq.get(ch, 0) + 1

        count = 0

        for value in freq.values():
            if value > 1:
                count += 1

        return count
    
def main():
    solver = CountOfDuplicateElementInString()
    string = "aadfsssreweeegggg"
    result = solver.countDuplicateElement(string)
    print(result)

if __name__ == "__main__":
    main()
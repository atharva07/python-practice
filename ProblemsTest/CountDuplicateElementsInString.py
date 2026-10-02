class CountDuplicateElementsInString:
    def countDuplicateElement(self, string: str) -> int:
        freq = {}
        
        for char in string:
            freq[char] = freq.get(char, 0) + 1

        count = 0
        for value in freq.values():
            if value > 1:
                count += 1

        return count 
    
def main():
    solver = CountDuplicateElementsInString()
    string = "aadfsssreweeegggg"
    result = solver.countDuplicateElement(string)
    print(result)

if __name__ == "__main__":
    main()
        
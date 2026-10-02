class MostFrequentCharacterInString:

    def mostFrequentCharacter(self, string: str) -> str:
        freq = {}

        for ch in string:
            freq[ch] = freq.get(ch, 0) + 1
        
        maxcount = 0
        mostFrequentChar = ""

        for key, value in freq.items():
            if value > maxcount:
                maxcount = value
                mostFrequentChar = key
        
        return mostFrequentChar
    
def main():
    solver = MostFrequentCharacterInString()
    string = "aadfsssreweeegggg"
    result = solver.mostFrequentCharacter(string)
    print(result)

if __name__ == "__main__":
    main()
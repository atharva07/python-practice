class CapitalizeFirstWordEachLetter:

    def capitalizeWord(self, string: str) -> str:
        words = string.split(' ')
        res = []

        for word in words:
            if word[0].lower():
                word = word[0].upper() + word[1:]
            res.append(word)

        return ' '.join(res)
    
def main():
    solver = CapitalizeFirstWordEachLetter()
    string = "senior qa engineer"
    result = solver.capitalizeWord(string)
    print(result)

if __name__ == "__main__":
    main()
class CapitalizeFirstWordOfEachLetter:
    def capitalize(self, string: str) -> str:
        words = string.split(' ')
        res = []
    
        # for word in words:
        #     if word[0] >= 'a' and word[0] <= 'z':
        #         word = word[0].upper() + word[1:]
        #     res.append(word)
        # return ' '.join(res)
    
        for word in words:
            if word[0].lower():
                word = word[0].upper() + word[1:]
            res.append(word)

        return ' '.join(res)

def main():
    solver = CapitalizeFirstWordOfEachLetter()
    string = "senior qa engineer"
    result = solver.capitalize(string)
    print(result)

if __name__ == "__main__":
    main()
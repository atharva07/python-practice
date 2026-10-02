class RemoveStringSentence:

    def removeDuplicateSentence(self, string: str) -> str:
        words = string.split(' ')
        result = []

        for word in words:
            freq = {}
            res = []
            for ch in word:
                freq[ch] = freq.get(ch, 0) + 1

            for key, value in freq.items():
                if value == 1:
                    res.append(key)

            word1 = ''.join(res)
            result.append(word1)
            
        return ' '.join(result)
    
def main():
    solver = RemoveStringSentence()
    string = "Senior QA Engineer"
    result = solver.removeDuplicateSentence(string)
    print(result)

if __name__ == "__main__":
    main()

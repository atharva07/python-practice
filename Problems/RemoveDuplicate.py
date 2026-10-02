class RemoveDuplicate:

    def removeDuplicate(self, string: str) -> str:
        freq = {}
        result = []

        for ch in string:
            freq[ch] = freq.get(ch, 0) + 1

        for key, value in freq.items():
            if value == 1:
                result.append(key)

        return ''.join(result)
    
def main():
    solver = RemoveDuplicate()
    string = "wordseddsee"
    result = solver.removeDuplicate(string)
    print(result)

if __name__ == "__main__":
    main()
    


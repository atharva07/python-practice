from typing import List
from collections import Counter

class FindDuplicateElementsInSentence:

    def findDuplicates(self, string: str) -> List:
        words = string.split(' ')
        result = []
        freq = {}

        for word in words:
            for char in word:
                freq[char] = freq.get(char, 0) + 1

        for key, value in freq.items():
            if value > 1:
                result.append(key)

        return result
    
    def findDuplicatesCounter(self, string1: str) -> List:
        count = Counter(string1)
        res = []

        for char in string1:
            if count[char] > 1:
                res.append(char)
        
        return res
    
def main():
    solver = FindDuplicateElementsInSentence()
    string = "Java isap latformi111111end 000 666 entla bsbcascvgsvchgnguage"
    result = solver.findDuplicatesCounter(string)
    print(result)

if __name__ == "__main__":
    main()        
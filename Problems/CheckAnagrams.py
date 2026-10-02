class CheckAnagrams:
    # Method 1 - Complexity: O(n) where n is the length of the strings
    def isAnagram(self, string1: str, string2: str) -> bool:
        freq1 = {} 
        freq2 = {}

        for ch in string1:
            freq1[ch] = freq1.get(ch, 0) + 1
        
        for ch in string2:
            freq2[ch] = freq2.get(ch, 0) + 1

        return freq1 == freq2
    
    # Method 2 - Complexity: O(n log n) due to sorting
    def isAnagramZip(self, string1: str, string2: str) -> bool:
        if len(string1) != len(string2):
            return False

        for a, b in zip(sorted(string1), sorted(string2)):
            if a != b:
                return False
            
        return True
    
def main():
    solver = CheckAnagrams()
    str1 = "silent"
    str2 = "listen"
    res1 = solver.isAnagram(str1, str2)
    res2 = solver.isAnagramZip(str1, str2)
    print(res1)
    print(res2)

if __name__ == "__main__":
    main()

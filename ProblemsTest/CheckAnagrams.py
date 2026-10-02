class CheckAnagrams:
    def isAnagram(self, string1: str, string2: str) -> bool:
        if len(string1) != len(string2):
            return False
        
        freq1 = {}
        freq2 = {}

        for ch in string1:
            freq1[ch] = freq1.get(ch, 0) + 1
        
        for ch in string2:
            freq2[ch] = freq2.get(ch, 0) + 1

        if len(freq1) == len(freq2):
            return True
        
        return False
    
    def isAnagramOptimized(self, string1: str, string2: str) -> bool:
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
    #res2 = solver.isAnagramZip(str1, str2)
    print(res1)
    #print(res2)

if __name__ == "__main__":
    main()
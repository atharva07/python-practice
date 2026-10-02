class LongestSubStringWithoutDuplicate:
    def longestSubstringBrute(self, string):
        n = len(string)
        max_len = 0
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if string[j] in seen:
                    break
                seen.add(string[j])
                max_len = max(max_len, j - i + 1)
        
        return max_len
    
    def longestSubStringOptimized(self, string):
        left = 0
        max_len = 0
        char_set = set()

        for right in range(len(string)):
            if string[right] in char_set:
                char_set.remove(string[left])
                left += 1
            
            char_set.add(string[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
def main():
    sol = LongestSubStringWithoutDuplicate()
    s = "abcabccbb"
    res = sol.longestSubstringBrute(s)
    print(res)

if __name__ == "__main__":
    main()
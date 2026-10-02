class LongestSubStringExactlyKDistinctChars:
    def longestSubstring(self, string, k):
        if len(string) == 0:
            return 0
        
        freq = {}
        for ch in string:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(string)):
            ch = string[i]
            if freq[ch] < k:
                left = self.longestSubstring(string[:i], k)
                right = self.longestSubstring(string[i+1:], k)
                return max(left, right)
        
        return len(string)
    
def main():
    sol = LongestSubStringExactlyKDistinctChars()
    s = "aaabb"
    k = 3
    res = sol.longestSubstring(s, k)
    print(res)

if __name__ == "__main__":
    main()

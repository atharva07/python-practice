class LongestSubstringExactlyKDistinctChars:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if freq[ch] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
            
        return len(s)
        
def main():
    sol = LongestSubstringExactlyKDistinctChars()
    s = "aaabb"
    k = 3
    res = sol.longestSubstring(s, k)
    print(res)

if __name__ == "__main__":
    main()
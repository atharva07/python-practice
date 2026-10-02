class LongestSubStringWithKMostChars:
    def longestSubstringKmost(self, string, k):
        if len(string) == 0:
            return 0
        
        freq = {}
        left = 0
        max_len = 0
        
        for right in range(len(string)):
            freq[string[right]] = freq.get(string[right], 0) + 1

            while len(freq) > k:
                freq[string[left]] -= 1
                if freq[string[left]] == 0:
                    del freq[string[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

def main():
    sol = LongestSubStringWithKMostChars()
    s = "eceba"
    k = 2
    res = sol.longestSubstringKmost(s, k)
    print(res)

if __name__ == "__main__":
    main()
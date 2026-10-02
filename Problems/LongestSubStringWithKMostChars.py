class LongestSubStringWithKMostChars:
    def longest_k_distinct(self, string: str, k: int) -> int:
        left = 0
        freq = {}
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
    
    def longestKMostSubString(self, string1, k):
        freq = {}
        max_len = 0
        left = 0

        for right in range(len(string1)):
            freq[string1[right]] = freq.get(string1[right], 0) + 1

            while len(freq) > k:
                freq[string1[left]] -= 1
                if freq[string1[left]] == 0:
                    del freq[string1[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
def main():
    sol = LongestSubStringWithKMostChars()
    s = "eceba"
    k = 2
    res = sol.longest_k_distinct(s, k)
    print(res)

if __name__ == "__main__":
    main()

class LongestRepeatingCharReplacement:
    def character_replacement(self, string: str, k: int) -> int:
        left = 0
        freq = {}
        max_len = 0
        max_freq = 0

        for right in range(len(string)):
            freq[string[right]] = freq.get(string[right], 0) + 1
            max_freq = max(max_freq, freq[string[right]])
            window_size = right - left + 1
            replacement_needed = window_size - max_freq
            
            # Check if invalid window. Replacement needed should always be less that or equal to k
            if replacement_needed > k:
                freq[string[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len
    
    def char_replacecment(self, string1, k):
        freq = {}
        max_freq = 0
        max_len = 0
        left = 0

        for right in range(len(string1)):
            freq[string1[right]] = freq.get(string1[right], 0) + 1
            max_freq = max(max_freq, freq[string1[right]])
            window_size = right - left + 1
            replacement_needed = window_size - max_freq

            if replacement_needed > k:
                freq[string1[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
def main():
    sol = LongestRepeatingCharReplacement()
    s = "AABABBA"
    k = 1
    res = sol.character_replacement(s, k)
    print(res)

if __name__ == "__main__":
    main()
class LongestRepeatingCharacterReplacement:
    def longestRepeatingChar(self, string: str, k: int) -> int:
        left = 0
        freq = {}
        max_len = 0
        max_freq = 0

        for right in range(len(string)):
            char = string[right]
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])
            window_size = right - left + 1
            replacement_needed = window_size - max_freq

            if replacement_needed > k:
                freq[string[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
def main():
    sol = LongestRepeatingCharacterReplacement()
    s = "AABABBA"
    k = 1
    res = sol.longestRepeatingChar(s, k)
    print(res)

if __name__ == "__main__":
    main()
from collections import defaultdict
from typing import List

# Time Complexity - O(n * k * log(k))
class GroupAnagrams():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            anagram_map[sorted_s].append(s)

        return list(anagram_map.values())
    
    def groupAnagrams(self, string: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
    
        for word in string:
            key = tuple(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())
    
def main():
    sol = GroupAnagrams()
    arr = ["eat","tea","tan","ate","nat","bat"]
    res = sol.groupAnagrams(arr)
    print(res)

if __name__ == "__main__":
    main()
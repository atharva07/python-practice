from typing import List

class FindAllMissingNumber:
    def findmissingNum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        result = []
        for i in range(1, n+1):
            if i not in freq:
                result.append(i)

        return result
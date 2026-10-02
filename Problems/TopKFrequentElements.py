from typing import List

class TopKFrequentElements:
    def kFrequentElements(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(freq[i][0])
        
        return res

def main():
    nums = [1,1,1,2,2,3]
    k = 2
    sol = TopKFrequentElements()
    result = sol.kFrequentElements(nums, k)
    print(result)

if __name__ == "__main__":
    main()
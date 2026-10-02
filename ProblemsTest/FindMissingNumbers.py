from typing import List

class FindMissingNumbers:
    def missingNumber(self, nums: List[int]) -> List:
        n = len(nums)

        res = []
        min_num = min(nums)
        max_num = max(nums)
        for i in range(min_num, max_num):
            if i not in nums:
                res.append(i)

        return res
    
def main():
    solver = FindMissingNumbers()
    nums = [1, 2, 3, 4, 5]
    result = solver.missingNumber(nums)
    print(result)

if __name__ == "__main__":
    main()

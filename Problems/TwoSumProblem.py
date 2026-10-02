from typing import List

class TwoSumProblem:
    # complexity: O(n^2)
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == k:
                    return [nums[i], nums[j]]
                
    # complexity: O(log n) - This approach is using Binary Search
    def twoSumOptimized(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            left = i + 1
            right = n - 1
            needed = k - nums[i]

            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == needed:
                    return [nums[i], nums[mid]]
                elif nums[mid] < needed:
                    left = mid + 1
                else:
                    right = mid - 1

        return []

def main():
    sol = TwoSumProblem()
    arr = [3,2,4]
    target = 6
    res = sol.twoSumOptimized(arr, target)
    print(res)

if __name__ == "__main__":
    main()
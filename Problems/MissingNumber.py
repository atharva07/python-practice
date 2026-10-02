from typing import List

class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sum = n * (n + 1) // 2
        s2 = 0
        for i in range(n-1):
            s2 += nums[i]

        missing = sum - s2
        return missing
    
def main():
    sol = MissingNumber()
    nums = [1,2,4]
    result = sol.missingNumber(nums)
    print(result)

if __name__ == "__main__":
    main()
from typing import List

class ReverseArray:
    def reverseArray(self, nums: List) -> List:
        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
    
    def reverseArray2(self, nums: List) -> List:
        res = []

        for i in range(len(nums) - 1, -1, -1):
            res.append(nums[i])

        return res
    
def main():
    solver = ReverseArray()
    nums = [1,2,3,4,5]
    result = solver.reverseArray(nums.copy())
    result2 = solver.reverseArray2(nums.copy())
    print(result)
    print(result2)

if __name__ == "__main__":
    main()
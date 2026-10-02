from typing import List

class RotateArrayByKPlaces:

    # this is left rotation
    def rotateListLeft(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        k = k % len(nums)

        # Copy all items in temp till len of d
        temp = []
        for i in range(k):
            temp.append(nums[i])

        # now copy the items of arr from index d in arr
        for i in range(k, len(nums)):
            nums[i - k] = nums[i]
        
        # Now copy the remaining items
        for i in range(len(nums) - k, len(nums)):
            nums[i] = temp[i - (len(nums) - k)]

        return nums
    
    # this is right rotation
    def rotateListRight(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        n = len(nums)
        k = k % n

        temp = []

        # Store last k elements
        for i in range(n-k, n):
            temp.append(nums[i])

        # Shift remaining elements
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        
        # copy the temp into arr to beginning
        for i in range(k):
            nums[i] = temp[i]

        return nums

def main():
    sol = RotateArrayByKPlaces()
    nums = [1,2,3,4,5]
    k = 2
    result = sol.rotateListLeft(nums, k)
    print(result)

if __name__ == "__main__":
    main()
from typing import List

class NextGreaterElement:
    # Brute Force
    def greaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # here we are assigning element as -1 in result
        # it will be [-1, -1, -1, -1]
        result = [-1] * n

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    result[i] = nums[j]
                    break
        
        return result
    
    def greaterElementOptimal(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]

            stack.append(i)

        return result    
    
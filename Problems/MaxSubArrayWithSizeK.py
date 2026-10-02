from typing import List

class MaxSumSubArrayWithSizeK:

    def maxSubArray(self, arr: List[int], k: int) -> int:
        windowSum = sum(arr[:k])
        max_sum = windowSum

        for right in range(k, len(arr)):
            windowSum += arr[right]
            windowSum -= arr[right - k]
            max_sum = max(max_sum, windowSum)

        return max_sum
    
def main():
    sol = MaxSumSubArrayWithSizeK()
    arr = []
    
if __name__ == "__main__":
    main()
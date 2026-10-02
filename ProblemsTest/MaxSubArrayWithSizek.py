class MaxSubArrayWithSizeK:
    def maxSubArraySizeL(self, arr, k):
        if len(arr) < k:
            return 0
        
        windowSum = sum(arr[:k])
        max_sum = windowSum

        for right in range(k, len(arr)):
            windowSum += arr[right]
            windowSum -= arr[right - k]
            max_sum = max(max_sum, windowSum)

        return max_sum
    
def main():
    sol = MaxSubArrayWithSizeK()
    arr = [1, 2, 3, 4, 5]
    k = 2
    res = sol.maxSubArraySizeL(arr, k)
    print(res)

if __name__ == "__main__":
    main()
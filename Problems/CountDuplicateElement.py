from typing import List

class CountDuplicateElement:
    def countDuplicateElement(self, arr: List[int]) -> int:
        count = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    count += 1

        return count
    
    def countDuplicateElementUsingDict(self, arr: List[int]) -> int:
        count = 0
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for key, value in freq.items():
            if value > 1:
                count += 1
        
        return count
        
def main():
    solver = CountDuplicateElement()
    number = [1,2,3,4,4,5,5,6,6,7,8,9]
    result = solver.countDuplicateElement(number)
    print(result)

if __name__ == "__main__":
    main()
from typing import List

class MoveZerosToEnd:
    def moveZeros(self, arr: List[int]) -> List:
        temp = []

        # Move all non-zero element to the temp
        for i in range(len(arr)):
            if arr[i] != 0:
                temp.append(arr[i])

        # replace arr element with temp
        for i in range(len(temp)):
            arr[i] = temp[i]

        nz = len(temp)

        # append zero to the end of arr
        for i in range(nz, len(arr)):
            arr[i] = 0

        return arr 
    
    def moveZerosOptimized(self, arr: List[int]) -> List:
        count = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        while count < len(arr):
            arr[count] = 0
            count += 1

        return arr
        
    
def main():
    solver = MoveZerosToEnd()
    arr = [1,2,0,3,0,4,0,0,5,6]
    result = solver.moveZerosOptimized(arr)
    print(result)

if __name__ == "__main__":
    main()
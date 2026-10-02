from typing import List

class SecondLargest:
    def secondLargest(self, arr: List[int]) -> int:
        largest = arr[0]
        slargest = -1

        for i in range(len(arr)):
            if arr[i] > largest:
                slargest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > slargest:
                slargest = arr[i]

        return slargest
    
def main():
    arr = [12, 35, 1, 10, 34, 1]
    solver = SecondLargest()
    res = solver.secondLargest(arr)
    print(res)

if __name__ == '__main__':
    main()      
from typing import List

class CountDuplicateElement:
    def countDuplicateElement(self, arr: List[int]) -> int:
        freq = {}

        for ele in arr:
            freq[ele] = freq.get(ele, 0) + 1
       
        count = 0
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
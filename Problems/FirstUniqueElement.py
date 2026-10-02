from typing import List

class FirstUniqueElement:
    def uniqueElement(self, arr: List[int]):
        freq_count = {}

        for num in arr:
            freq_count[num] = freq_count.get(num, 0) + 1

        for key, value in freq_count.items():
            if value == 1:
                return key

def main():
    sol = FirstUniqueElement()
    arrr = [2, 3, 4, 2, 3, 5, 4]
    res = sol.uniqueElement(arrr)
    print(res)

if __name__ == "__main__":
    main()
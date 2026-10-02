from typing import List

class FindCommonStringInLists:
    def find_common_string(self, str1: str, str2: str) -> List:
        common = []
        for item in str1:
            if item in str2 and item not in common:
                common.append(item)

        return common
    
def main():
    solver = FindCommonStringInLists()
    str1 = ["apple", "banana", "single", "Laxmi", "Raghu"]
    str2 = ["june", "july", "apple", "april", "Laxmi"]
    result = solver.find_common_string(str1, str2)
    print(result)
    
if __name__ == "__main__":
    main()
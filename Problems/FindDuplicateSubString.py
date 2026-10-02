from typing import List

class FindDuplicateSubString:
    def findDuplicatesubstring(self, string: str) -> str:
        seen = set()
        duplicates = set()
        n = len(string)

        for i in range(n):
            for j in range(i+1, n+1):
                substr = string[i:j]

                if substr in seen:
                    duplicates.add(substr)
                else:
                    seen.add(substr)

        longsub = list(duplicates)
        long_string = max(longsub, key=len)
        return long_string
    
def main():
    sol = FindDuplicateSubString()
    s = "banana"
    res = sol.findDuplicatesubstring(s)
    print(res)

if __name__ == "__main__":
    main()
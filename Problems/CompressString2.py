from itertools import groupby
from typing import List

class CompressString2:
    def compress(self, string: str) -> List:
        s = string.strip()
        print(s)
        res = []
        
        for key, group in groupby(s):
            count = len(list(group))
            res.append((count, int(key)))

        return res
    
def main():
    sol = CompressString2()
    string = "1222311"
    result = sol.compress(string)
    print(result)

if __name__ == "__main__":
    main()

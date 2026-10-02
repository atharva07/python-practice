from itertools import groupby
from typing import List

class CompressString:
    def compressString(self, string1: str) -> List:
        s = string1.strip()
        res = []

        for key, group in groupby(s):
            count = len(list(group))
            res.append((count, int(key)))

        return res

def main():
    sol = CompressString()
    string = "1222311"
    result = sol.compressString(string)
    print(result)

if __name__ == "__main__":
    main()
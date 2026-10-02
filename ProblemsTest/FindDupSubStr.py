class FindDupSubStr:
    def duplicateSubstr(self, string) -> str:
        seen = set()
        duplicate = set()
        n = len(string)

        for i in range(n):
            for j in range(i+1, n+1):
                substr = string[i:j]

                if substr in seen:
                    duplicate.add(substr)
                else:
                    seen.add(substr)

        dup_list = list(duplicate)

        long_substr = max(dup_list, key=len)

        return long_substr
    
def main():
    sol = FindDupSubStr()
    s = "banana"
    res = sol.duplicateSubstr(s)
    print(res)

if __name__ == "__main__":
    main()

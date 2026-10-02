class CheckRotationsCountTarget:
    def checkRotationsCount(self, string1: str, string2: str) -> int:
        if len(string1) != len(string2):
            return -1
        
        # this is using left rotations
        for i in range(len(string1)):
            if string1 == string2:
                return i
            string1 = string1[1:] + string1[0]

        return -1
    
def main():
    sol = CheckRotationsCountTarget()
    string1 = "abcde"
    string2 = "deabc"
    result = sol.checkRotationsCount(string1, string2)
    print(result)

if __name__ == "__main__":
    main()
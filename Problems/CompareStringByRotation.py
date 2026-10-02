class CompareStringByRotation:
    def rotateCompareString(self, string1: str, string2: str) -> bool:
        if len(string1) != len(string2):
            return False
        
        for i in range(len(string1)):
            if string1 == string2:
                return True
            
            # this is left rotation
            string1 = string1[1:] + string1[0]
            # this is right rotation
            # string1 = string1[-1] + string1[:-1]

        return False
    
def main():
    sol = CompareStringByRotation()
    string1 = "abcde"
    string2 = "deabc"
    result = sol.rotateCompareString(string1, string2)
    print(result)

if __name__ == "__main__":
    main()
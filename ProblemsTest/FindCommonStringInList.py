class FindCommonStringInList:
    def findCommonString(self, string1, string2):
        common = []

        for item in string1:
            if item in string2 and item not in common:
                common.append(item)

        return common
    
def main():
    solver = FindCommonStringInList()
    str1 = ["apple", "banana", "single", "Laxmi", "Raghu"]
    str2 = ["june", "july", "apple", "april", "Laxmi"]
    result = solver.findCommonString(str1, str2)
    print(result)
    
if __name__ == "__main__":
    main()
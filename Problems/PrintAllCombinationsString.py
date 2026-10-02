class PrintAllCombinationsString:
    def combinations_iterative(self, s):
        result = [""]

        for char in s:
            new_subset = []
            for subset in result:
                new_subset.append(subset + char)
            result.extend(new_subset)
        
        return [x for x in result if x]
    
def main():
    sol = PrintAllCombinationsString()
    string1 = "abc"
    result = sol.combinations_iterative(string1)
    print(result)

if __name__ == "__main__":
    main()
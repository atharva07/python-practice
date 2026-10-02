class FindPermutations:
    def find_permutations(self, string):
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return
            
            for i in range(len(remaining)):
                backtrack(path + remaining[i], remaining[:i]+remaining[i+1:])

        backtrack("", string)
        return result

def main():
    string = "abc"
    sol = FindPermutations()
    res = sol.find_permutations(string)
    print(res)

if __name__ == "__main__":
    main()
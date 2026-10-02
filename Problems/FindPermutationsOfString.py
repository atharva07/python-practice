from typing import List

class FindPermutationsOfString:
    def find_permutations(self, string: str) -> List:
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return 
            
            for i in range(len(remaining)):
                backtrack(path + remaining[i], remaining[:i] + remaining[i+1:])
        
        backtrack("", string)
        return result
    
    # using recursive insertion method
    def find_permutations_recursive(self, string: str) -> List:
        if len(string) == 1:
            return [string]
        
        first = string[0]
        perms = self.find_permutations_recursive(string[1:])

        result = []

        for perm in perms:
            for i in range(len(perm) + 1):
                result.append(perm[:i] + first + perm[i:])
        
        return result
    
def main():
    sol = FindPermutationsOfString()
    res = sol.find_permutations("abc")
    print(res)

if __name__ == "__main__":
    main()
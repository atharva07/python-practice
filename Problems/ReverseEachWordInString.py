class ReverseEachWordInString:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = []
        
        for word in words:
            chars = list(word)
            left = 0
            right = len(chars) - 1

            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

            re = ''.join(chars)
            res.append(re)
        
        return ' '.join(res)

    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = []

        for word in words:
            chars = list(word)
            left = 0
            right = len(chars) - 1

            while left < right:
                chars[left], chars[right] = chars[right], chars[left]

                left += 1
                right -= 1

            re = ''.join(chars)
            res.append(re)

        return ' '.join(res)
    
    def reverseStringOptimized(self, s: str) -> str:
        words = s.split(' ')
        res = [word[::-1] for word in words]
        return ' '.join(res)

def main():
    solver = ReverseEachWordInString()
    #string = "Senior QA Engineer"
    string = "abc de f"
    result = solver.reverseWords(string)
    result1 = solver.reverseStringOptimized(string)
    print(result)
    print(result1)

if __name__ == "__main__":
    main()
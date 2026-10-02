class FindSumOfDigitsInString:
    def findSum(self, string: str) -> int:
        sum = 0

        for ch in string:
            if ch.isdigit():
                sum += int(ch)

        return sum
    
    def returnNumber(self, string: str) -> int:
        numbers = []

        for char in string:
            if char.isdigit():
                numbers.append(int(char))

        res = ''.join(map(str, numbers))
        return int(res)
    
    def returnLargestDigit(self, string: str) -> int:
        largest = 0

        for char in string:
            if char.isdigit():
                largest = max(largest, int(char))

        return largest

    def replaceDigitWithStar(self, string: str) -> str:
        result = []

        for char in string:
            if char.isdigit():
                result.append("*")
            else:
                result.append(char)
        
        return ''.join(result)
    
    def checkPalindromInDigit(self, string: str) -> bool:
        result = []

        for char in string:
            if char.isdigit():
                result.append(int(char))

        res = ''.join(map(str, result))

        if res == res[::-1]:
            return True
        return False

def main():
    solver = FindSumOfDigitsInString()
    string = "abc123"
    result = solver.replaceDigitWithStar(string)
    print(result)

if __name__ == "__main__":
    main()
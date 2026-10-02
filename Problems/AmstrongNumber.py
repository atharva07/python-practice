import math

class AmstrongNumber:
    
    def findArmstrongNumber(self, number: int) -> bool:
        k = len(str(number))
        sum = 0
        n = number

        while n > 0:
            ld = n % 10
            sum += math.pow(ld, k)
            n = n // 10

        return sum == number
    
    def findArmstrongNum(self, number: int) -> bool:
        k = len(str(number))
        sum = 0
        n = number

        while n > 0:
            ld = n % 10
            sum += math.pow(ld, k)
            n = n // 10

        return sum == number

def main():
    solver = AmstrongNumber()
    number = 153
    result = solver.findArmstrongNumber(number)
    print(result)

if __name__ == "__main__":
    main()

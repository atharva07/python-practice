import math

class ArmstrongNumber:
    # A Number which is sum of its cube of each number
    def findArmstrong(self, num: int) -> bool:
        k = len(str(num))
        sum = 0
        n = num

        while n > 0:
            single_num = n % 10
            sum += math.pow(single_num, k)
            n = n // 10
        
        return sum == num
    
def main():
    solver = ArmstrongNumber()
    number = 153
    result = solver.findArmstrong(number)
    print(result)

if __name__ == "__main__":
    main()
            

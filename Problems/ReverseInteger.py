class ReverseInteger:

    def reverse(self, x: int) -> int:
        res = 0
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = int(str(x)[1:][::-1]) * -1

        if res > 2**31 -1 or res < -2**31:
            return 0
        
        return res
    
    def reverseIntegerGood(self, x: int) -> int:
        temp = x
        digits = len(str(x))

        reverse = 0

        for _ in range(digits):
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10
    
        return reverse
        
def main():
    sol = ReverseInteger()
    x = 123
    res = sol.reverse(x)
    print(res)

if __name__ == "__main__":
    main()
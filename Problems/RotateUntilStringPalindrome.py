class RotateUntilStringPalindrome:
    def isPalindrome(self, string: str) -> bool:
        return string == string[::-1]
    
    def rotateString(self, string: str) -> int:
        n = len(string)
        rotated = string

        for i in range(n):
            if self.isPalindrome(rotated):
                return i

            rotated = rotated[1:] + rotated[0]

        return -1   
        

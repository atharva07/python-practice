from typing import List

class RotateStringByKPlaces:
    def rotateString(self, string: str, k: int) -> str:
        if not string:
            return string
        
        words = list(string)
        print(words)

        k = k % len(string)
        print(k)

        # copy all the chars till len of k in temp
        temp = []
        for i in range(k):
            temp.append(words[i])

        print(temp)

        # now copy the items of arr from index k in arr
        for i in range(k, len(words)):
            words[i - k] = words[i]

        # Now copy the remaining items
        for i in range(len(words) - k, len(words)):
            words[i] = temp[i - (len(words) - k)]

        return ''.join(words)
    
def main():
    sol = RotateStringByKPlaces()
    string = "abcdef"
    k = 3
    result = sol.rotateString(string, k)
    print(result)

if __name__ == "__main__":
    main()
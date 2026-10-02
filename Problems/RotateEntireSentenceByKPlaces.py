class RotateEntireSentenceByKPlaces:
    def rotateString(self, string: str, k: int) -> str:
        words = string.split(' ')

        k = k % len(words)

        temp = []
        for i in range(k):
            temp.append(words[i])

        for i in range(k, len(words)):
            words[i-k] = words[i]

        for i in range(len(words)-k, len(words)):
            words[i] = temp[i - (len(words) - k)]

        return ' '.join(words)
    
def main():
    sol = RotateEntireSentenceByKPlaces()
    string = "I love coding very much"
    k = 2
    result = sol.rotateString(string, k)
    print(result)

if __name__ == "__main__":
    main()
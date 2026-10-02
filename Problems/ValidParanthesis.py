class ValidParentheses:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch == ")" and stack[-1] == "(":
                    stack.pop()
                if ch == "]" and stack[-1] == "[":  
                    stack.pop()
                if ch == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
    
def main():
    obj = ValidParentheses()
    print(obj.isValid("()"))
    print(obj.isValid("()[]{}"))
    print(obj.isValid("(]"))
    print(obj.isValid("([)]"))
    print(obj.isValid("{[]}"))

if __name__ == "__main__":
    main()
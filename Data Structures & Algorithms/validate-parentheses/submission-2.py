class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] == key[char]:
                    stack.pop()
                else:
                    return False
        return not stack
        
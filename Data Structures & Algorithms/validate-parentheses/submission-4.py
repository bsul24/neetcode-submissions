class Solution:
    def isValid(self, s: str) -> bool:
        key = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in key:
                if not stack:
                    return False
                if key[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
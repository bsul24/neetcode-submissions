class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for el in s:
            if el == ")" or el == "}" or el == "]":
                if len(stack) == 0:
                    return False
                if key[stack[len(stack) - 1]] != el:
                    return False
                stack.pop()
            else:
                stack.append(el)
        return len(stack) == 0
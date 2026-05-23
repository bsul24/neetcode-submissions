class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for sym in s:
            if sym in pairs:
                stack.append(sym)
            else:
                if not stack:
                    return False
                if pairs[stack[-1]] == sym:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

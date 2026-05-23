class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if left == right:
                return True

            if not self.isAlphaNum(s[left]):
                left += 1
                continue
            
            if not self.isAlphaNum(s[right]):
                right -= 1
                continue

            if left + 1 == right:
                if s[left].lower() == s[right].lower():
                    return True

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
            

    def isAlphaNum(self, c):
        return c.isascii() and c.isalnum()
    

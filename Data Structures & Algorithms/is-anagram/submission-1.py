class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}

        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1

        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1

        

        return s_count == t_count

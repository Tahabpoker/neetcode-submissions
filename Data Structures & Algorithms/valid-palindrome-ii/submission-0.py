class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(s: str) -> bool:
            return s == s[::-1]
        
        for i in range(len(s)):
            new_s = s[:i] + s[i+1:]
            if is_pal(new_s):
                return True
        return False
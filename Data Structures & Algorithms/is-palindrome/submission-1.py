import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub('[^A-Za-z0-9]+', '', s)
        new_s = new_s.lower()
        n = len(new_s)
                
        l, r = 0, n-1

        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True


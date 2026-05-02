import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub('[^A-Za-z0-9]+', '', s)
        new_s = new_s.lower()
        return new_s == new_s[::-1]
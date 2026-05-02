class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = s.copy()

        for i in range(len(s)):
            s[i] = stack.pop()

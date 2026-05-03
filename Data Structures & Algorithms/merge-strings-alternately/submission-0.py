class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0 
        new_word = ""
        while l < len(word1) and r < len(word2):
            new_word += word1[l] 
            new_word += word2[r]
            l += 1
            r += 1
        if l < len(word1):
            for i in range(l, len(word1)):
                new_word += word1[i]

        if r < len(word2):
            for i in range(r, len(word2)):
                new_word += word2[i]
        return new_word

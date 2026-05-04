class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ""

        for s in strs:
            n = len(s)
            new_strs += str(n) + "Ø" + s
        
        return new_strs
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "Ø":
                j += 1
           
            length = int(s[i:j])

            word = s[j+1:j+1+length]
            res.append(word)

            i = j + 1 + length
        
        return res
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        seen = dict()

        for s in strs:
            for i in range(1,len(s)+1):
                if s[0:i] not in seen:
                    seen[s[0:i]] = 1
                else:
                    seen[s[0:i]] += 1
        best = "" 
        for prefix, count in seen.items():
            if count == len(strs) and len(prefix) > len(best):
                best = prefix
        
        return best
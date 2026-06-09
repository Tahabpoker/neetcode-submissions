class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            res = 0 
            for j in range(32):
                if (1 << j) & i:
                    res += 1

            result.append(res)
        return result
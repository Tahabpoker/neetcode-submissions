class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = f"{n:032b}"
        return int(bin_n[::-1], 2)
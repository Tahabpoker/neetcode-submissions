class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        num_bin = bin(n)
        for i in range(len(num_bin)):
            if num_bin[i] == "1":
                ones += 1

        return ones
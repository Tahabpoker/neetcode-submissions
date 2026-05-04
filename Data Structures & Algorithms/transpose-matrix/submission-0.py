import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        np_arr = np.array(matrix)
        res =  np_arr.T
        return res.tolist()
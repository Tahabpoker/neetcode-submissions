from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top = count.most_common(k)
        top_k = []

        for i in range(k):
            top_k.append(top[i][0])
        
        return top_k 

class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[mid:])
        right = self.merge_sort(arr[:mid])

        return self.merge(left, right)

    def merge(self, left, right):
        sorted_list = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else: 
                sorted_list.append(right[j])
                j += 1
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list
        
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
    
    
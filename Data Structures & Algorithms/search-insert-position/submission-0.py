class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        index, mid = len(nums), 0
        
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                index = mid
                r = mid - 1
        return index
    
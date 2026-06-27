class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 1, x, 0
        while l <= r:
            mid = (l + r) >> 1
            if mid * mid == x:
                ans = mid
                break
            elif mid * mid < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
                
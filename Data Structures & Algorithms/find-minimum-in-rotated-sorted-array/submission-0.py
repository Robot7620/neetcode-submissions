class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        ans = nums[0]
        while lo <= hi:
            mid = (hi+lo)//2
            if nums[lo] < nums[hi]:
                ans = min(ans, nums[lo])
                break
            ans = min(ans, nums[mid])
            if nums[mid] < nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

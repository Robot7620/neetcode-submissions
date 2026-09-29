import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        ans = hi
        while lo <= hi:
            mid = lo + (hi-lo)//2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            
            if time <= h:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
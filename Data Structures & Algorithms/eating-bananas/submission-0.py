class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            k = (l + r) // 2
            hours = sum((p + k - 1) // k for p in piles)
            if hours <= h:
                ans = k          # k works: record it, try slower
                r = k - 1
            else:
                l = k + 1        # too slow: need faster
        return ans
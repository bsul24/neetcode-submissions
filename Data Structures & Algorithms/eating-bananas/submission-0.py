class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        cur = high

        while low <= high:
            mid = (low + high) // 2
            if self.speedTest(piles, h, mid):
                cur = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return cur


    def speedTest(self, piles, h, k):
        for pile in piles:
            h -= math.ceil(pile / k)
        if h >= 0:
            return True
        return False


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        bottom = 1 # lowest speed
        top = max(piles) # highest speed

        while top > bottom:
            middle = (bottom + top) // 2 # middle speed (binary search)
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/middle) # hours it takes at each "middle" speed
            if hours <= h:
                top = middle
            else:
                bottom = middle+1

        return bottom
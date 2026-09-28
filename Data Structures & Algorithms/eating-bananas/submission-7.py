class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min hour will be len(piles)
        # trying to find the min k that can eat all bananas within h hours
        # for each of the number we'd want to find ronud up value of n / k
        #however there's some info we already know if k*h < sum of all piles then it's not possible we can skip the first few k to get start with, k >= sum / h
        l , r = 1, max(piles)
        
        while l < r:
            c = l + (r - l) // 2

            hours = 0
            for num in piles:
                hours += math.ceil(num / c)

            if hours <= h:
                r = c
            else:
                l = c + 1
            
        return l
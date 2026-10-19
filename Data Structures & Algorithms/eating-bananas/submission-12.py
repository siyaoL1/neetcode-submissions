class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for num in piles:
                hours += math.ceil(num / mid)
            
            if hours <= h:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1

        return result

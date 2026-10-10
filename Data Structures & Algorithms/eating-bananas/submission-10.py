class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for count in piles:
                hours += (count + mid - 1) // mid
                # hours += math.ceil(count / mid)
            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result


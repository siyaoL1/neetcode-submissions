class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1, max(piles)
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            required_hours = 0
            for num in piles:
                required_hours += math.ceil(num / mid)
            if required_hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return result

            


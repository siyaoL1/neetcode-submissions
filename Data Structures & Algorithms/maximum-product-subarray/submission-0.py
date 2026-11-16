class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_max = nums[0]
        results = [(nums[0], nums[0])]
        for i in range(1, len(nums)):
            prev_max, prev_min = results[i - 1]
            x = nums[i]
            candidates = (prev_max * x, prev_min * x, x)
            curr_max = max(candidates)
            curr_min = min(candidates)
            results.append((curr_max, curr_min))
            max_max = max(max_max, curr_max)
        
        return max_max

            

        
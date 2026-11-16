class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = prev_max = prev_min = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            candidates = (prev_max * x, prev_min * x, x)
            prev_max = max(candidates)
            prev_min = min(candidates)
            result = max(result, prev_max)

        return result
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(nums[i] + i, max_reach)
        
        return True
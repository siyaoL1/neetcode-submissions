class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Idea:
        # We will have a stack of the index that we want to process for the nums that begins those index
        # Have a visited set that avoids duplicated visit
        # For each index we will add new index based on the possible jumps
        # for example if we have [1,2,0,1,0] and index 0 we will add index 1 only
        # then for the value 2 we will add index 2 and index 3 to the stack
        # we return true if we are able ot reach the len(nums) - 1
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False

            max_reach = max(nums[i] + i, max_reach)
        
        return True
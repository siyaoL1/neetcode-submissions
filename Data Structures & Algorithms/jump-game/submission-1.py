class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Idea:
        # We will have a stack of the index that we want to process for the nums that begins those index
        # Have a visited set that avoids duplicated visit
        # For each index we will add new index based on the possible jumps
        # for example if we have [1,2,0,1,0] and index 0 we will add index 1 only
        # then for the value 2 we will add index 2 and index 3 to the stack
        # we return true if we are able ot reach the len(nums) - 1
        stack = [0]
        visited = {0}

        while stack:
            index = stack.pop()
            if index >= len(nums) - 1:
                return True
            for step in range(1, nums[index] + 1):
                if index + step not in visited:
                    stack.append(index + step)
                    visited.add(index + step)
        
        return False
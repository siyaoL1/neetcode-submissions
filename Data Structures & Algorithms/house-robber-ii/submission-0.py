class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(index, prev_robbed, first_robbed):
            # Check last house
            if index == len(nums) - 1:
                if not prev_robbed and not first_robbed:
                    return nums[index]
                else:
                    return 0
            
            # Check visited
            if (index, prev_robbed, first_robbed) in memo:
                return memo[(index, prev_robbed, first_robbed)]
            
            # Rob based on prev_robbed
            if prev_robbed:
                result = helper(index + 1, False, first_robbed)
            else:
                result = max(
                    nums[index] + helper(index + 1, True, first_robbed if index != 0 else True),
                    helper(index + 1, False, first_robbed)
                )
            
            memo[(index, prev_robbed, first_robbed)] = result
            return result

        return helper(0, False, False)
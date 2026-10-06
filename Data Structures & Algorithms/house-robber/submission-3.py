class Solution:
    def rob(self, nums: List[int]) -> int:
        last_two, last_one = 0, 0

        for i in range(len(nums)):
            curr = max(last_two + nums[i], last_one)
            last_two = last_one
            last_one = curr
        
        return last_one


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best = [nums[0], max(nums[0], nums[1])]

        house = 2
        while house < len(nums):
            best.append(max(best[house - 2] + nums[house], best[house - 1]))
            house += 1

        return best[-1]
        

# 1 2 3 4 5 6 7 8 9
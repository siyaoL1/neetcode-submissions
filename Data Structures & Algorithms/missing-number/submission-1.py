class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0

        for expected in range(len(nums) + 1):
            missing ^= expected

        for actual in nums:
            missing ^= actual
        return missing
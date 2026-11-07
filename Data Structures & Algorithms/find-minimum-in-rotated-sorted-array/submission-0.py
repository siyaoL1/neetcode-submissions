class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        while l <= r:
            c = l + (r - l) // 2
            if nums[c] < nums[r]:
                res = c
                r = c
            else:
                l = c + 1
        
        return nums[res]
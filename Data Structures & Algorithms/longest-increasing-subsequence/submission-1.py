class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev_index):
            if i == len(nums):
                return 0
            if (i, prev_index) in memo:
                return memo[(i, prev_index)]
            if prev_index != -1 and nums[i] <= nums[prev_index]:
                result = dfs(i + 1, prev_index)
            else:
                result = max(1 + dfs(i + 1, i), dfs(i + 1, prev_index))
            memo[(i, prev_index)] = result
            return result
        return dfs(0, -1)

        
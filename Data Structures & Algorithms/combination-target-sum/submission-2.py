class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       # to find the complete solution set trying out all combination results in 2^n complexity, actually more since we can use duplicated number so it's unbounded thats why I think it will be easier for us to build the result list bottom up from 1 to the target
        res = []
        cur = []

        def dfs(i, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i, total + nums[i])
            cur.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res

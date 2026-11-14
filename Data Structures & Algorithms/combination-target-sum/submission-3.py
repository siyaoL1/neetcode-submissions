class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        candidates = sorted(nums)
        result = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remaining:
                    break

                path.append(num)
                dfs(i, remaining - num)
                path.pop()

        dfs(0, target)
        return result
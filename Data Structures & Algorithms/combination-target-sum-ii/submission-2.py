class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            for j in range(i, len(candidates)):
                if candidates[j] > remaining:
                    return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                cur.append(candidates[j])
                dfs(j + 1, remaining - candidates[j])
                cur.pop()
        
        dfs(0, target)
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        
        def dfs(i, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            prev = None
            for j in range(i, len(candidates)):
                if candidates[j] > remaining:
                    return
                if prev and prev == candidates[j]:
                    continue
                prev = candidates[j]
                cur.append(candidates[j])
                dfs(j + 1, remaining - candidates[j])
                cur.pop()
        
        dfs(0, target)
        return res
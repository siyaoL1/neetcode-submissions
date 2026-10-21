class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        results = [[]]

        for num in nums:
            new_results = []
            for perm in results:
                for i in range(len(perm) + 1):
                    new_perm = perm[:i] + [num] + perm[i:]
                    new_results.append(new_perm)

            results = new_results
        return results

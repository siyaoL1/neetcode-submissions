class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            prev_len = len(result)
            for i in range(prev_len):
                result.append(result[i] + [num])
        
        return result
            
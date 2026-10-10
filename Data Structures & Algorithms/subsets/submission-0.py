class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            curr_len = len(result)
            for i in range(curr_len):
                result.append(result[i] + [num])
        
        return result




test_cases = [
    [[], [[]]],
    [[1], [[], [1]]],
    [[1, 2], [[], [1], [2], [1, 2]]]
]

solution = Solution()

for nums, expected in test_cases:
    result = solution.subsets(nums)
    assert result == expected, f"Failed nums:{nums}, result:{result}, expected:{expected}"
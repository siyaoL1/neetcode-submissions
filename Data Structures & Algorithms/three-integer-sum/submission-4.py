class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # why not just do every pair like two sum? since we 
        # will require O(N) per num so it will be O(N^2) where as
        # if we sort ahead it will be O(nlogn) and for all element it 
        # will still be N^2 to find? so it's still n^2
        result = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, length - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

test_cases = [
    ([-1, -1, 2, 3], [[-1, -1, 2]]),
    ([-1, -1, 1], []),
    ([-1, -1, 2, 2], [[-1, -1, 2]]),
    ([-1, -1, 2, 2, -4], [[-4, 2, 2], [-1, -1, 2]]),
]

solution = Solution()
for nums, expected in test_cases:
    result = solution.threeSum(nums)
    assert result == expected, f"FAILED nums:{nums}, result:{result}, expected:{expected}"
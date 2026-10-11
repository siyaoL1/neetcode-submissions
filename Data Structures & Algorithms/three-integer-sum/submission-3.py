class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # why not just do every pair like two sum? since we 
        # will require O(N) per num so it will be O(N^2) where as
        # if we sort ahead it will be O(nlogn) and for all element it 
        # will still be N^2 to find? so it's still n^2
        result = set()
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    right -= 1
                    left += 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return [list(triplet) for triplet in result]

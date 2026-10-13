class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        result = -1
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
                left, right = num - 1, num + 1
                while left in nums_set:
                    nums_set.remove(left)
                    left -= 1
                while right in nums_set:
                    nums_set.remove(right)
                    right += 1
                result = max((right - 1) - (left + 1) + 1, result)
        
        return result

                
                
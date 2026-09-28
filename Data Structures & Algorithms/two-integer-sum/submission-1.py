class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                other_index = seen[need]
                if other_index < i:
                    return [other_index, i]
                else:
                    return [i, other_index]
            seen[nums[i]] = i
        
        return []

        
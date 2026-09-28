class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_freq = {}
        indices = [0, 0]
        for i in range(len(nums)):
            num = nums[i]
            need = target - num
            if need in num_freq:
                indices = [i, num_freq[need][0]]
            if nums[i] not in num_freq:
                num_freq[num] = [i]
            else:
                num_freq[num].append(i)
        
        if indices[0] < indices[1]:
            return indices
        return [indices[1], indices[0]]

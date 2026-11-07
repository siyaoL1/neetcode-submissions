class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = [0] * 10000 * 2
        for num in nums:
            freq[num-10000] += 1
        
        for i in range(len(freq)):
            if freq[i] == 1:
                return i - 10000
        
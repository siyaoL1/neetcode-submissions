class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] =  freqs.get(num, 0) + 1
        
        frequency_slot = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            frequency_slot[freq].append(num)
        result = []
        freq = len(nums)
        while freq > 0 and k > 0:
            if frequency_slot[freq]:
                k -= len(frequency_slot[freq])
                result.extend(frequency_slot[freq])
            freq -= 1

        return result
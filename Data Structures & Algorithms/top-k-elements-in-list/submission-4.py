class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
            
        # build bucket
        freq_bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            freq_bucket[freq].append(num)
        
        index = len(freq_bucket) - 1
        counts = 0
        result = []
        while counts < k:
            counts += len(freq_bucket[index])
            result.extend(freq_bucket[index])
            index -= 1
        
        return result
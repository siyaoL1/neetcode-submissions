class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
        
        sorted_list = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        result = []
        for n in range(k):
            result.append(sorted_list[n][0])
        return result
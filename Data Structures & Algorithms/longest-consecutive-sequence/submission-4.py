class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length_map = {}
        for num in nums:
            if num not in length_map:
                left = num - length_map.get(num - 1, 0)
                right = num + length_map.get(num + 1, 0)
                merged_length = right - left + 1
                length_map[num] = merged_length
                length_map[left] = merged_length
                length_map[right] = merged_length
        
        result = -1
        for num, length in length_map.items():
            result = max(result, length)

        return result

                
                
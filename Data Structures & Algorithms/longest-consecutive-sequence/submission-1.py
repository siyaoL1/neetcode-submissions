class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length_map = {}
        for num in nums:
            if num not in length_map:
                if num - 1 in length_map and num + 1 in length_map:
                    left = num - 1 - (length_map[num - 1] - 1)
                    right = num + 1 + (length_map[num + 1] - 1)
                    length_map[num] = right - left + 1
                    length_map[left] = right - left + 1
                    length_map[right] = right - left + 1
                elif num - 1 in length_map:
                    left = num - 1 - (length_map[num - 1] - 1) 
                    length_map[left] += 1
                    length_map[num] = length_map[left]
                elif num + 1 in length_map:
                    right = num + 1 + (length_map[num + 1] - 1)
                    length_map[right] += 1
                    length_map[num] = length_map[right]
                else:
                    length_map[num] = 1
        
        result = -1
        for num, length in length_map.items():
            result = max(result, length)

        return result

                
                
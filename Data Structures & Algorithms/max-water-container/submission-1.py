class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The amount of water can be expressed as
        # min(heights[i], heights[j]) * (j - i)
        # where j >= i
        # we can have two pointer walking throuh and calculate pairs
        # but this is not sorted how do we gurantee we can move forward
        # we should move the shorter one since the taller one guarantees to be able to catch the same volumn after the move
        i, j = 0, len(heights) - 1
        max_water = -1

        while i < j:
            curr_water = min(heights[i], heights[j]) * (j - i)
            max_water = max(max_water, curr_water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_water

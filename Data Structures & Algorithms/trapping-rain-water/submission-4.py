class Solution:
    # Idea:
    # Go from the first non zero height value in the array and set that as a left pointer,
    # the try to find the right pointer where it's at least as high as it
    # in the same time trying to capture the water that's trapped while moving the second pointer
    # Then we would move the first pointer to second pointer, second pointer to be second pointer + 1
    # If we don't find a valid second pointer then we don't add the temp water we've conuted to the res
    def trap(self, height: List[int]) -> int:
        left, right = 0, 0

        while left < len(height) and height[left] == 0:
            left += 1
        right = left + 1
        if left >= len(height):
            return 0

        left_height = height[left]
        res_water = 0
        temp_water = 0
        while left <= len(height) - 3:
            if right >= len(height):
                height[left] -= 1
                temp_water = 0
                right = left
            elif height[right] >= height[left]:
                # print(res_water, temp_water, left, right, height[left])
                res_water += temp_water
                temp_water = 0
                left = right
            else:
                temp_water += height[left] - height[right]
            
            right += 1
        return res_water



        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Idea:
        # Search the turning point of max to min
        # binary search with left and right pointer
        # if mid < left => right = mid
        # if mid > right => left = mid
        # then the question becomes can any value be right < mid < left?
        # the answer is no since that means we have more than one inflection point between max and min

        # after finding th inflection point, we can shift it back to a normal array or doing binary search in place

        # Find inflection point
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # we've found that the array is shifted
        shifted = left
        #binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            print(nums[(mid + shifted) % len(nums)])
            if nums[(mid + shifted) % len(nums)] == target:
                return (mid + shifted) % len(nums)
            elif nums[(mid + shifted) % len(nums)] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
# 0,1,2,4,5,6,7
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the rotated times
        rotate_times = 0
        left, right = 0, len(nums) - 1
        if nums[left] > nums[right]:
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
        rotate_times = left
        def rotate(index):
            return (index + rotate_times) % len(nums)
            
        # binary search for the target
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[rotate(mid)] == target:
                return rotate(mid)
            elif nums[rotate(mid)] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
        
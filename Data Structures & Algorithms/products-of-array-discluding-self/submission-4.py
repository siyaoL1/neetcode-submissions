class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]


        #[1, 1, 2, 8]
        # calculate left side products
        for i in range(len(nums) - 1):
            result.append(result[-1] * nums[i])

        suffix_prod = 1
        for i in range(len(nums) - 1, -1, - 1):
            result[i] *= suffix_prod
            suffix_prod *= nums[i]
            
        return result
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count >= 2:
                    return [0] * len(nums)
            else:
                total_product *= num
        print(total_product)

        product_list = []
        for num in nums:
            if num == 0:
                product_list.append(total_product)
            else:
                if zero_count != 0:
                    product_list.append(0)
                else:
                    product_list.append(total_product // num)
        
        return product_list
            
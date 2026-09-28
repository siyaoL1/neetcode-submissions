class Solution:
    def productExceptSelfDivision(self, nums: List[int]) -> List[int]:
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

    def productExceptSelf_v2(self, nums: List[int]) -> List[int]:
        left_product = [1] 

        for i in range(len(nums) - 1):
            left_product.append(left_product[-1] * nums[i])

        nums.reverse()
        right_product = [1]
        for i in range(len(nums) - 1):
            right_product.append(right_product[-1] * nums[i])
        right_product.reverse()

        return [left_product[i] * right_product[i] for i in range(len(nums))]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] 

        for i in range(len(nums) - 1):
            result.append(result[-1] * nums[i])

        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        # print(result)

        return result










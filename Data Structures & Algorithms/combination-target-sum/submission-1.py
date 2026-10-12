class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       # to find the complete solution set trying out all combination results in 2^n complexity, actually more since we can use duplicated number so it's unbounded thats why I think it will be easier for us to build the result list bottom up from 1 to the target
        dp = []

        for curr_target in range(target + 1):
            curr_result = []                
            for num in nums:
                requires = curr_target - num
                if requires == 0:
                    curr_result.append([curr_target])
                elif requires > 0 and dp[requires]:
                    for prev_result in dp[requires]:
                        if num >= prev_result[-1]:
                            curr_result.append(prev_result + [num])
            dp.append(curr_result)

        process_result = set([tuple(sorted(seq)) for seq in dp[target]])

        return [list(seq) for seq in process_result]

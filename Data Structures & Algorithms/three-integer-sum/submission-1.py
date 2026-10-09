class Solution:
    def threeSumTimeout(self, nums: List[int]) -> List[List[int]]:
        # Reduce the problem to be two sum by calculating the first two sums
        two_sums = {} # sum => [(indices)]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                curr = nums[i] + nums[j]
                if curr in two_sums:
                    two_sums[curr].append([i, j])
                else:
                    two_sums[curr] = [[i, j]]

        three_sums = []
        for i in range(len(nums)):
            need = 0 - nums[i]
            if need in two_sums:
                for pair in two_sums[need]:
                    if i not in pair:
                        three_sums.append(sorted([nums[i], nums[pair[0]], nums[pair[1]]]))

        result = set()
        for indices in three_sums:
            result.add(tuple(indices))

        return list(result)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1


        return list(result)
        
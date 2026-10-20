class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = {()}
        nums.sort()
        # Idea:
        # We are walking through each number in the nums adding new subset
        # can be created with this number by iterating each existing subset and inserting the value and add it to the subset set.
        # At the end I will convert the subset set to a list with list

        for num in nums:
            new_subsets = set()
            new_subsets = {subset + (num,) for subset in subsets}
            subsets.update(new_subsets)
            
        return [list(subset) for subset in subsets]
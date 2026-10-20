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
            for subset in subsets:
                new_subset = list(subset)
                new_subset.append(num)
                new_subset = tuple(new_subset)
                new_subsets.add(new_subset)
            for new_subset in new_subsets:
                subsets.add(new_subset)
        
        return [list(subset) for subset in subsets]
class Solution:
    def merge_first_attempt(self, intervals: List[List[int]]) -> List[List[int]]:
        # First thought is that we can either process the intervals or process the entire range
        # If we want to reduce the intervals into a minimal set, we should find ways to process each pair while comparing the existig intervals which will end up be worst case O(n^2) if the intervals are all non-overlapping
        # IF we want to simply map out a whole range with 0 being missing 1 being present, we still are going through each pair once, but the mapping operation can take up O(m) where m is the max size of the end in this canse 1000, so O(nm) as well
        # Since the constrants are intervals length and end both 1000, it doesn't quite matter that much , but the second approach will require extra O(m) space
        # I think the second solution is simpler so I'll do that one

        whole_range = [0] * 1001
        for start, end in intervals:
            for i in range(start, end):
                whole_range[i] = 1
        result = []
        start = -1
        for i in range(len(whole_range)):
            if whole_range[i]:
                if start == -1:
                    start = i
            else:
                if start != -1:
                    result.append([start, i])
                    start = -1
        
        if start != -1:
            result.append([start, len(whole_range) - 1])

        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # assuming I'm allowed to modify the intervals
        results = []
        for start, end in intervals:
            if results and results[-1][1] >= start:
                results[-1] = [results[-1][0], max(results[-1][1], end)]
            else:
                results.append([start, end])
        
        return results
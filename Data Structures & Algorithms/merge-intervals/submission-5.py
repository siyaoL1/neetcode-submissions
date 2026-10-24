class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Idea: Sort the intervals based on interval openning values
        # Then walk through each element if we see curr[left] <= prev[right], we should merge them as [prev[left], max(curr[right], prev[right])] Then continue the iteration until we have no more to merge
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = result[-1]
            curr = intervals[i]
            if prev[1] >= curr[0]:
                prev[1] = max(curr[1], prev[1])
            else:
                result.append(curr)

        return result
        
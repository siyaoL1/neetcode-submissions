class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = None
        result = 0

        for start, end in intervals:
            if not prev_end is None and start < prev_end:
                result += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        
        return result
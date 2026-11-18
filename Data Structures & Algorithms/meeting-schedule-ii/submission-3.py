"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals_list = [(i.start, i.end) for i in intervals]
        intervals_list.sort()
        heap = []
        for start, end in intervals_list:
            if heap and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)
        return len(heap)
                
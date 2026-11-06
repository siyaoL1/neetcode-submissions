"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = [(i.start, i.end) for i in intervals]
        intervals.sort()
        result = 0
        rooms = []
        for interval in intervals:
            added = False
            if rooms and rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
        
        return len(rooms)
        
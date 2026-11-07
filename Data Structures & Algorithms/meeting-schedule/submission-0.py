"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        pairs = [(i.start, i.end) for i in intervals]

        pairs.sort()

        prev_end = None
        for start, end in pairs:
            if prev_end and prev_end > start:
                return False
            prev_end = end
        
        return True

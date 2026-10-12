class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []

        for curr_left, curr_right in intervals:
            if result:
                prev_left, prev_right = result[-1]
                if curr_left <= prev_right:
                    result[-1] = [prev_left, max(prev_right, curr_right)]
                else:
                    result.append([curr_left, max(prev_right, curr_right)])
            else:
                result.append([curr_left, curr_right])
        return result

            
        
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        new_left, new_right = newInterval

        for left, right in intervals:
            if inserted or right < new_left:
                result.append([left, right])
            elif new_right < left:
                result.append([new_left, new_right])     
                result.append([left, right])
                inserted = True
            else:
                new_left = min(new_left, left)
                new_right = max(new_right, right) 
                
        if not inserted:
            result.append([new_left, new_right])

        return result
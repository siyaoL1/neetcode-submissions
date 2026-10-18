class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        merged = False
        new_left, new_right = newInterval
        for interval in intervals:
            if not merged:
                # if strictly smaller
                if new_right < interval[0]:
                    result.append([new_left, new_right])     
                    result.append(interval)
                    merged = True
                elif interval[1] < new_left:
                    result.append(interval)
                else:
                    new_left = min(new_left, interval[0])
                    new_right = max(new_right, interval[1]) 
            else:
                result.append(interval)   
              
                
        if not merged:
            result.append([new_left, new_right])

        return result
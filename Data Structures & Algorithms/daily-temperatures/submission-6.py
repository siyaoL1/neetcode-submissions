class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        h = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while h and h[0][0] < curr:
                temp, index = heapq.heappop(h)
                result[index] = i - index
            heapq.heappush(h, (curr, i))
        
        return result

                 


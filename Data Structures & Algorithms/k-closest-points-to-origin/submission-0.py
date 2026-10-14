class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        x2, y2 = 0, 0
        for x1, y1 in points:
            heapq.heappush(heap, (math.sqrt((x1 - x2)**2 + (y1 - y2)**2), [x1, y1]))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]

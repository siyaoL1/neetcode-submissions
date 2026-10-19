import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        heap = stones.copy() # Max heap
        heapq.heapify_max(heap)

        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            diff = abs(x - y)
            if diff:
                heapq.heappush_max(heap, diff)
        
        if heap:
            return heap[0]
        return 0

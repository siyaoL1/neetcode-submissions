import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_k = list(nums) # Min heap
        self.heap_remain = [] # Map heap

        heapq.heapify(self.heap_k)
        
        while len(self.heap_k) > k - 1:
            self.heap_remain.append(heapq.heappop(self.heap_k))
        heapq.heapify_max(self.heap_remain)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_k, val)
        num = heapq.heappop(self.heap_k)
        heapq.heappush_max(self.heap_remain, num)

        return self.heap_remain[0]

        

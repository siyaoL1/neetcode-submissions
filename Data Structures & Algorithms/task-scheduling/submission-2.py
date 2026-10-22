import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = {}
        for task in tasks:
            if task in task_dict:
                task_dict[task] += 1
            else:
                task_dict[task] = 1
        
        heap = []
        for task, times in task_dict.items():
            heap.append((times, task))
        heapq.heapify_max(heap)

        counter = 0
        cooldown = deque()
        while heap or cooldown:
            # print(counter, heap, cooldown)
            # Increment cycle
            if not heap:
                counter = cooldown[0][0]
            else:
                counter += 1

            # Clear available items
            while (cooldown and cooldown[0][0] <= counter):
                ready_at, remaining_count, task = cooldown.popleft()
                heapq.heappush_max(heap, (remaining_count, task))
                
            # Execute task
            times, value = heapq.heappop_max(heap)
            times -= 1
            if times:
                cooldown.append([counter + n + 1, times, task])
        
        return counter
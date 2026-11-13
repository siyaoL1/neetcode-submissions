import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DFS and keep a shortest distance to all nodes and keep a visited set
        nodes = {}

        for ui, vi, ti in times:
            neighbors = nodes.setdefault(ui, {})
            neighbors[vi] = ti

        visited = {}
        heap = [(0, k)]

        while heap:
            existing_distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = existing_distance

            for neighbor, distance in nodes.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(heap, (existing_distance + distance, neighbor))
        
        if len(visited) != n:
            return -1
        
        return max(visited.values())
                
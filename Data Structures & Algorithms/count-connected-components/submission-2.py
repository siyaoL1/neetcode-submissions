class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Construct adjacency list
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # print(adj)
        visited = set()
        count = 0
        for node in range(n):
            if node in visited:
                continue
            count += 1
            stack = [node]
            visited.add(node)
            while stack:
                curr_node = stack.pop()
                for neighbor in adj[curr_node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
            
        return count
        
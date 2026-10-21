class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        stack = [0]
        visited = {0}
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                adj[neighbor].remove(node)
                if neighbor in visited:
                    return False
                stack.append(neighbor)
                visited.add(neighbor)
        
        if len(visited) != n:
            return False
        return True
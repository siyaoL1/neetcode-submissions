class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Construct adjacency list
        adj = {}
        for a, b in edges:
            adj.setdefault(a, []).append(b)
            adj.setdefault(b, []).append(a)
        # print(adj)
        visited = set()
        count = 0
        for node in adj.keys():
            if node in visited:
                continue
            # print(f"node: {node}, visited: {visited}")
            count += 1
            stack = [node]
            while stack:
                # print(f"stack: {stack}")
                curr_node = stack.pop()
                # print(f"curr_node: {curr_node}")
                visited.add(curr_node)
                for neighbor in adj[curr_node]:
                    # print(f"neighbor: {neighbor}")
                    if neighbor not in visited:
                        stack.append(neighbor)
            
        return count + (n - len(visited))
        
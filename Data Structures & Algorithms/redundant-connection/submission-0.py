class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return [a, b]

            if size[a] < size[b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = parent[root_a]
            size[root_a] += size[root_b]

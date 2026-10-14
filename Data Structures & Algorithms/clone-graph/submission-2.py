"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Recursively check if the current node is None if not construct a new node with recursive call for each of the neibors 
        # one important thing to ensure is that there's no cycle and no isolated nodes since the input is just one node I assume we don't need to worry about the later one but a cycle will break this approach and we need a visited set
        # OK this doesn't really work since the neighbors are inclusive on both endpoint, that will natrually cause duplicated cycles we do need a visited 
        if not node:
            return None
        
        remaining = [node]
        visited = set()
        cloned_nodes = {}

        while remaining:
            curr_node = remaining.pop()
            cloned_neighbors = []
            for neighbor in curr_node.neighbors:
                # Haven't processed, add to process queue
                if neighbor.val not in visited:
                    remaining.append(neighbor)
                
                # Populate current node's neighbor
                if neighbor.val not in cloned_nodes:
                    cloned_nodes[neighbor.val] = Node(neighbor.val, [])
                cloned_neighbors.append(cloned_nodes[neighbor.val])
            # Mark current node as processed
            visited.add(curr_node.val)
            if curr_node.val not in cloned_nodes:
                cloned_nodes[curr_node.val] = Node(curr_node.val, cloned_neighbors)
            else:
                cloned_nodes[curr_node.val].neighbors = cloned_neighbors
            
        return cloned_nodes[node.val]

        
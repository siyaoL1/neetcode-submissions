"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        to_clone = [node]
        cloned_nodes = {}
        
        
        while to_clone:
            
            curr_node = to_clone.pop()
            cloned_neighbors = []
            
            # Clone and construct cloned_neighbors
            for neighbor in curr_node.neighbors:
                if neighbor not in cloned_nodes:
                    cloned_neighbor = Node(neighbor.val, None)
                    cloned_nodes[neighbor] = cloned_neighbor
                    cloned_neighbors.append(cloned_neighbor)
                    to_clone.append(neighbor)
                else:
                    cloned_neighbors.append(cloned_nodes[neighbor])
            
            if curr_node in cloned_nodes:
                cloned_nodes[curr_node].neighbors = cloned_neighbors
            else:
                cloned_nodes[curr_node] = Node(curr_node.val, cloned_neighbors)


        return cloned_nodes[node]
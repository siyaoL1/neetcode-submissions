"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        reference = {}
        new_head = Node(head.val, head.next, head.random)
        reference[head] = new_head

        node = new_head
        while node.next:
            next_node = node.next
            new_next_node = Node(next_node.val, next_node.next, next_node.random)
            reference[next_node] = new_next_node
            node.next = new_next_node
            node = node.next
        
        node = new_head
        while node:
            if node.random:
                node.random = reference[node.random]
            node = node.next
        
        return new_head

        
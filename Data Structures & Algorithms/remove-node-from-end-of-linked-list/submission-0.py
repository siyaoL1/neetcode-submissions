# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def helper(node):
            if not node:
                return None, 1

            new_next, from_end = helper(node.next)

            if from_end == n:
                return new_next, from_end + 1
            
            node.next = new_next
            return node, from_end + 1
        
        return helper(head)[0]
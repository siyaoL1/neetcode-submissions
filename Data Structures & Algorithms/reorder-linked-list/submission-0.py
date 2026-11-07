# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        refs = []
        node = head
        while node:
            refs.append(node)
            node = node.next
        
        node = refs[0]
        left, right = 1, len(refs) - 1
        while left < right:
            node.next = refs[right]
            node = node.next
            right -= 1
            node.next = refs[left]
            node = node.next
            left += 1
        
        if left == right:
            node.next = refs[left]
            node = node.next
        
        node.next = None

        
            
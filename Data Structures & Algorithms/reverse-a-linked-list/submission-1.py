# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseListStack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack = []
        count = 0
        while head:
            stack.append(head)
            head = head.next

        new_head = stack.pop()
        curr = new_head
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        return new_head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr, next_node = None, head, head.next

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
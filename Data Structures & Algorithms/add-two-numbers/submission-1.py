# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        carry = 0
        
        while l1 or l2 or carry:
            curr_sum = carry
            if l1:
                curr_sum += l1.val
            if l2:
                curr_sum += l2.val
            curr_node = ListNode(curr_sum % 10, None)
            if not prev:
                head = curr_node
                prev = curr_node
            else:
                prev.next = curr_node
                prev = curr_node
            if curr_sum >= 10:
                carry = 1
            elif carry:
                carry = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head
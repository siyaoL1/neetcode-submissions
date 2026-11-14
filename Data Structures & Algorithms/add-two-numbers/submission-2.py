# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            curr_sum = carry
            if l1:
                curr_sum += l1.val
            if l2:
                curr_sum += l2.val
            curr_node = ListNode(curr_sum % 10, None)

            tail.next = curr_node
            tail = curr_node
            carry, digit = divmod(curr_sum, 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
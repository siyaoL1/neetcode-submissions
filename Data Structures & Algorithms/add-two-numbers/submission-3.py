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
            if carry == 0 and (l1 is None or l2 is None):
                tail.next = l1 if l1 is not None else l2
                break

            curr_sum = carry
            if l1:
                curr_sum += l1.val
            if l2:
                curr_sum += l2.val
            carry, digit = divmod(curr_sum, 10)
            
            curr_node = ListNode(digit, None)
            tail.next = curr_node
            tail = curr_node
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
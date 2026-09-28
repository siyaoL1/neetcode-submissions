# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2: 
            return list1
        
        if list1.val < list2.val:
            result = self.duplicate(list1)
            list1 = list1.next
        else:
            result = self.duplicate(list2)
            list2 = list2.next
        head = result
        while list1 and list2:
            if list1.val < list2.val:
                result.next = self.duplicate(list1)
                list1 = list1.next
            else:
                result.next = self.duplicate(list2)
                list2 = list2.next
            result = result.next
        
        if list1:
            result.next = list1
        elif list2:
            result.next = list2
        
        return head

        
    
    def duplicate(self, node):
        return ListNode(node.val, node.next)
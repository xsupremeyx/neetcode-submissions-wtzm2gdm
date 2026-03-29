# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        
        # Minor Cases:
        if (head1 == None) and (head2 == None):
            return None
        elif (head2 == None):
            return list1
        elif (head1 == None):
            return list2
        
        # Choose start
        if head1.val <= head2.val:
            start = head1
            head1 = head1.next
        else:
            start = head2
            head2 = head2.next
        
        curr = start

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                curr = head1
                head1 = head1.next
            else:
                curr.next = head2
                curr = head2
                head2 = head2.next
        if head1:
            curr.next = head1
        elif head2:
            curr.next = head2
        
        return start
        

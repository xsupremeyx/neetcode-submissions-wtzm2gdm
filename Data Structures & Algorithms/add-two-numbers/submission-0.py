# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,None)
        head1 = l1
        head2 = l2
        head = dummy
        carry = False
        while head1 or head2 or carry:
            val1 = 0
            val2 = 0
            if head1:
                val1 = head1.val
                head1 = head1.next

            if head2:
                val2 = head2.val
                head2 = head2.next


            sumation = val1 + val2 + carry
            sumNode = ListNode((sumation)%10,None)
            if(sumation >= 10):
                carry = True
            else:
                carry = False
            
            head.next = sumNode
            head = head.next
            
        return dummy.next
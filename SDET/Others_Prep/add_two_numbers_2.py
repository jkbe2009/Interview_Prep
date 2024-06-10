
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            op1 = l1.val if l1 else 0
            op2 =  l2.val if l2 else 0
            val = op1 + op2 + carry
            carry = 0
            if val > 9:
                val = val % 10
                carry = 1
            curr.next = ListNode(val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
            
        return dummy.next
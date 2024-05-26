
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Calculate length A
        lenA = 0
        curr = headA
        while curr:
            curr = curr.next
            lenA += 1

        # Calculate length B
        lenB = 0
        curr = headB
        while curr:
            curr = curr.next
            lenB += 1
        
        if lenA >= lenB:
            diff = lenA - lenB
            curr1 = headA
            curr2 = headB
        else:
            diff = lenB - lenA
            curr1 = headB
            curr2 = headA
        
        while diff > 0:
            curr1 = curr1.next
            diff -= 1
        
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
        
        return None


        

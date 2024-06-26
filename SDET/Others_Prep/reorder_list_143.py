
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        def reverse(thead):
            if not thead or not thead.next:
                return thead
            
            temp = reverse(thead.next)
            thead.next.next = thead
            thead.next = None
            return temp
        
        def merge(l1, l2):
            dummy = ListNode(-1)
            curr = dummy
            while l2:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                curr.next = l2
                l2 = l2.next
                curr = curr.next
            curr.next = l1
                
            return dummy.next
        
        if not head or not head.next or not head.next.next:
            return head
        
        slow = fast = head
        l1 = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None

        l2 = reverse(l2)
        
        return merge(l1, l2)
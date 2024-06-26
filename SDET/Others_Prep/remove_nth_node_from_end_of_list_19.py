
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        def naive():
            if not head:
                return
            
            # get length l:
            curr = head
            l = 0
            while curr:
                l += 1
                curr = curr.next
            
            if l == n:
                return head.next
            
            curr = head
            # move l-n-1 times:
            for _ in range(l-n-1):
                curr = curr.next
            curr.next = curr.next.next
            
            return head
        
        def single_iteration():
            # Edge cases:
            if not head or not head.next:
                return None
            if not head.next.next:
                if n == 1:
                    head.next = head.next.next
                    return head
                elif n == 2:
                    return head.next
                else:
                    return None
            
            slow = head
            fast = head
            # Move the fast pointer n times:
            for _ in range(n):
                fast = fast.next
                if fast == None:
                    return head.next

            # Move both the pointers until fast is at the last node:
            while fast.next:
                slow = slow.next
                fast = fast.next
            
            # Remove the nth node from the last
            slow.next = slow.next.next

            return head
        
        def two_pointers():
            dummy = ListNode(-1)
            dummy.next = head

            # Edge cases:
            if not head or not head.next:
                return None
            
            fast = head
            slow = dummy
            # Move the fast pointer n times
            for _ in range(n):
                fast = fast.next
            
            # Move both the pointers by 1 until fast is null
            while fast:
                slow = slow.next
                fast = fast.next

            slow.next = slow.next.next
            return dummy.next
        
        # return naive()
        # return single_iteration()
        return two_pointers()
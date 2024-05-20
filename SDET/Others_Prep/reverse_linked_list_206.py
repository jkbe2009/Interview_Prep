# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverse_using_iteration(self, head):
        # Edge case:
        if head == None or head.next == None:
            return head
        
        prev = head
        curr = head.next
        prev.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

    def reverse_using_recursion(self, head):
        # Base Case:
        if head == None or head.next == None:
            return head

        # Recursive case:
        temp = self.reverse_using_recursion(head.next)
        head.next.next = head
        head.next = None
        return temp
        

    def reverse_using_stack(self, head):
        stack = []

        if head == None or head.next == None:
            return head

        curr = head
        while curr != None:
            stack.append(curr)
            curr = curr.next
        
        head = stack.pop()
        curr = head

        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        return head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # return self.reverse_using_stack(head)
        # return self.reverse_using_recursion(head)
        return self.reverse_using_iteration(head)
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev_ll_iterative(head):
            if head == None or head.next == None:
                return head

            st = []
            curr = head

            while curr:
                st.append(curr)
                curr = curr.next
            
            head = st.pop()
            prev = head
            
            while st:
                curr = st.pop()
                prev.next = curr
                prev = curr

            prev.next = None 
            return head

        def rev_ll_recursive(head):
            if head == None or head.next == None:
                return head
            
            new_head =  rev_ll_recursive(head.next)
            head.next.next = head
            head.next = None
            return new_head
            


        # return rev_ll_iterative(head)
        return rev_ll_recursive(head)
        
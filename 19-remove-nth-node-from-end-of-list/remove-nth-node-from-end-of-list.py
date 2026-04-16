# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        i = 1

        while cur and i <= n:
            cur = cur.next
            i += 1
        
        while cur:
            prev, cur = prev.next, cur.next
        
        temp = prev.next.next
        prev.next.next = None
        prev.next = temp

        return dummy.next

        
        
        
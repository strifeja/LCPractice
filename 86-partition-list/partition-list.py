# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        less = dummy
        dummy2 = ListNode()
        more = dummy2
        cur = head

        while cur:
            if cur.val < x:
                less.next = ListNode(cur.val)
                less = less.next
            else:
                more.next = ListNode(cur.val)
                more = more.next
            cur = cur.next
        
        less.next = dummy2.next
        return dummy.next
            
        

        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        for _ in range(left - 1):
            prev, cur = cur, cur.next

        start = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = start
            start, cur = cur, temp
        
        prev.next.next = cur
        prev.next = start
        return dummy.next

        
        
        
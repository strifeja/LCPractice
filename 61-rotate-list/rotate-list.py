# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        prev, cur = head, head
        length = 1

        while cur.next:
            length += 1
            cur = cur.next
        
        k = k % length
        cur.next = prev

        for _ in range(length-k-1):
            prev = prev.next
        
        temp = prev.next
        prev.next = None

        return temp

            
            


        
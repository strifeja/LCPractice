# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
            
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        while fast:
            if fast.next and fast.val == fast.next.val:
                val = fast.val
                while fast and fast.val == val:
                    fast = fast.next
                slow.next = fast
            else:
                slow, fast = slow.next, fast.next
        
        return dummy.next
        
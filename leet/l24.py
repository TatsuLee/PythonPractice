# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # create a fake head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            # swap
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            # link p with node number 2
            p.next = tmp
            p = p.next.next
        return dummy.next

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
        dummy = ListNode(None)
        dummy.next = head
        pHead = dummy
        while pHead.next and pHead.next.next:
            # swap node1 with node2
            node2 = pHead.next.next
            pHead.next.next = node2.next  # link node1 to node3
            node2.next = pHead.next  # link node2 to node1
            pHead.next = node2  # link head to node2
            # move pHead to node2
            pHead = pHead.next.next
        return dummy.next

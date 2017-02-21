# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None:
            return head
        n, counter = 1, head
        while counter.next:
            counter = counter.next
            n += 1
        if k % n == 0:
            return head  # k = len(list)
        elif k > n:
            k = k % n
        # find break point and reconnect
        i, prev = 1, head
        while i < n-k:
            prev = prev.next
            i += 1
        newhead = prev.next
        prev.next = None
        counter.next = head
        return newhead

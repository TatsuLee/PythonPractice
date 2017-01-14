#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        # find the median
        i = 1
        count = head
        while count is not None:
            count = count.next
            i += 1
        j = 1
        mid = i/2
        count = head
        while j <= mid:
            count = count.next
            j += 1
        # reverse the last half
        newhead = None
        current = count
        while current is not None:
            nxt = current.next
            current.next = newhead
            newhead = current
            current = nxt
        # compare the two
        while newhead is not None:
            if head.val != newhead.val:
                return False
            head = head.next
            newhead = newhead.next
        return True





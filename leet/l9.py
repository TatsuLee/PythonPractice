#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def isPalindrome(self, x):

        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xstr = str(x)
        if len(xstr) == 1:
            return True
        xhalf = len(xstr)/2
        for i, j in zip(xstr[:xhalf:1], xstr[:xhalf-1:-1]):
            if i != j:
                return False
        return True





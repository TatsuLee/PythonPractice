#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 0
        out = ''
        if x < 0:
            neg = 1
            x = x.__neg__()
        xstr = str(x)
        for i in xstr[::-1]:
            out += i
        if int(out) > 2**31-1:
            return 0
        if neg:
            return int(out).__neg__()
        else:
            return int(out)

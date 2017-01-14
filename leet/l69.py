#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in [0, 1]:
            return x
        shift = 31
        while x >> shift == 0:
            shift -= 1
        xn, prev = 2.0**(shift/2), 2.0**(shift/2+1)
        while abs(xn-prev) > .9:
            prev = xn
            xn = (xn + x/xn)/2.0
        return int(xn)

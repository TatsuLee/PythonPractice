#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for shift in range(32):
            if 1 << shift == n:
                return True
            elif 1 << shift > n:
                return False
        return False

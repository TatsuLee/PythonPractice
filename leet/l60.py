#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1: return str(n)
        elements, kPerm, = range(1,n+1), ''
        while True:
            index = int(k/(math.factorial(n-1)+.01))
            k = k%(math.factorial(n-1)+.01)
            n -= 1
            digit = elements[index]
            kPerm += str(digit)
            elements.remove(digit)
            if n == 1:
                kPerm += str(elements[0])
                return kPerm

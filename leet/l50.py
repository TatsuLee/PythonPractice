#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        product = 1
        if n==0:
            return product
        innerProd, shift, sign, n = x, 1, int(n < 0), abs(n)
        while n > 0:
            while n>>shift > 0:
                innerProd = innerProd*innerProd
                shift += 1
            n -= 1<<(shift-1)
            innerProd, shift, product = x, 1, product*innerProd
        if sign:
            return 1/product
        else:
            return product

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # question: how to prove this?
        i, nZero = 5, 0
        while n >= i:
            nZero += n / i
            i *= 5
        return nZero

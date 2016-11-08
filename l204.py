#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, sieve, sieve[:2] = 2, [True]*n, [False]*2
        while i*i < n:
            if sieve[i]:
                j = i*i
                while j < n:
                    sieve[j] = False
                    j += i
            i += 1
        return sum(sieve)

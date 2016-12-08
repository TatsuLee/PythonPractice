#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, prime = [1], [2, 3, 5]
        for k in range(n-1):
            temp = [i*j for i in s for j in prime]
            temp = list(set(temp))  # remove duplicates
            temp.sort()
            s.append(temp[k])
        return s[-1]

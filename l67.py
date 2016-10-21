#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        k, sumBin = 0, ''
        if a == '' or b == '':
            return max(a, b)
        if len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a
        else:
            b = '0'*(len(a)-len(b)) + b
        for i, j  in zip(a[::-1], b[::-1]):
            if i == j:
                sumBin = str(k) + sumBin
                k = int(i)
            else:
                sumBin = str(int(k!=1)) + sumBin
        if k:
            sumBin = '1' + sumBin
        return sumBin


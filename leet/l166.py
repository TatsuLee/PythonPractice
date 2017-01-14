#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype string: str
        """
        if numerator == 0:
            return '0'
        n, d = abs(numerator), abs(denominator)
        string = str(n/d)
        if (numerator < 0) ^ (denominator < 0):
            string = '-' + string
        r = n % d
        if r == 0:
            return string
        else:
            string += '.'
        rlist, fracstr = [r], ''
        while r:
            index = rlist.index(r)
            if index != len(rlist)-1:
                fracstr = fracstr[:index] + '(' + fracstr[index:] + ')'
                break
            fracstr += str(r*10/d)
            r = r*10 % d
            rlist.append(r)
        return string + fracstr

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign,INT_MAX = int(dividend*divisor<0),2**31
        dividend,divisor = abs(dividend),abs(divisor)
        if dividend < divisor:
            return 0
        if divisor ==0:
            return INT_MAX-1
        if divisor == 1:
            if sign:
                return -min(dividend,INT_MAX)
            else:
                return min(dividend,INT_MAX-1)
        qutient,shift = 0,31
        while shift >=0:
            if dividend >= divisor<<shift:
                dividend -= divisor<<shift
                qutient += 1<<shift
                if qutient == INT_MAX-1:
                    break
            shift -= 1
        if sign:
            return -qutient
        return qutient

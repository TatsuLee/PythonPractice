#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        string = str(numerator*1.0/denominator)
        dot = string.find('.')
        integer = string[:dot+1]  # with decimal point
        frac = string[dot+1:]
        if len(frac) < 12:
            return string
        for i in [0, 1, 2]:
            for j in [None, -1]:
                s = frac[i:j]
                repos = (s+s).find(s, 1, -1)
                if repos != -1:
                    return integer+frac[:i]+'('+s[:repos]+')'
        return string

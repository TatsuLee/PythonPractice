#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        out = 0
        for i in range(len(s)-1):
            if roman[s[i+1]] > roman[s[i]]:
                out -= roman[s[i]]
            else:
                out += roman[s[i]]
        return out+roman[s[-1]]



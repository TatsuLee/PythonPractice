#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {1: 'I',
                 5: 'V',
                 10: 'X',
                 50: 'L',
                 100: 'C',
                 500: 'D',
                 1000: 'M'}
        k = sorted(roman, reverse=True)
        out = ''
        for i in range(len(k)):
            while num >= k[i]:
                if num/k[i] == 4:
                    out += roman[k[i]]+roman[k[i-1]]
                    num -= 4*k[i]
                elif str(num)[0] == '9':
                    out += roman[k[i+1]]+roman[k[i-1]]
                    num -= 9*k[i+1]
                else:
                    out += roman[k[i]]
                    num -= k[i]
        return out




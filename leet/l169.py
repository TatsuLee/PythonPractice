#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for i, j in zip(s[::-1], range(len(s))):
            n += (ord(i)-64)*26**j
        return n

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return num
        mod = num % 9
        if mod == 0:
            return 9
        else:
            return mod

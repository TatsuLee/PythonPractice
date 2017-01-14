#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # remove trailing space
        str = str.strip()
        if not str:
            return 0
        i = 0
        if str[i] in ['+', '-']:
            i = 1
        if i >= len(str) or str[i] > '9' or str[i] < '0':
            return 0
        while i < len(str):
            if '0' <= str[i] <= '9':
                i += 1
            else:
                str = str[:i]
                break
        if int(str) > 2**31-1:
            return 2**31-1
        elif int(str) < -2**31:
            return -2**31
        else:
            return int(str)

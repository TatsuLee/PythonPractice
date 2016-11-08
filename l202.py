#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp, tlist, nstr = 0, [0], str(n)
        while True:
            if temp == 1:
                return True
            if tlist.index(temp) != len(tlist)-1:
                return False
            temp = 0
            for i in nstr:
                temp += int(i)**2
            nstr = str(temp)
            tlist.append(temp)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        else:
            return self.convertToTitle((n-1)/26) + chr(65+(n-1) % 26)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return '' 
        strs = sorted(strs, key=lambda x: len(x))
        out = strs[0]
        for i in strs[1:]:
            while not i.startswith(out):
                out = out[:-1]
        return out

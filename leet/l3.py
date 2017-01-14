#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def test(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 0:
            return 0
        else:
            r = s[0]
            best = 1
        for i in range(1, len(s)):
            idx = r.find(s[i])
            if idx == -1:
                r += s[i]
            else:
                best = max(len(r), best)
                r = r[idx+1:]+s[i]
        return max(len(r), best) 

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        out = s[0]
        for i in range(len(s)-1):
            l = len(out)/2
            tmp = self.palin(s, i, i)
            if len(tmp) > len(out):
                out = tmp
            if s[i] == s[i+1]:
                tmpdb = self.palin(s, i, i+1)
                if len(tmpdb) > len(out):
                    out = tmpdb
        return out

    def palin(self, s, left, right):
        while left > 0 and right < len(s)-1:
            if s[left-1] == s[right+1]:
                left -= 1
                right += 1
            else:
                return s[left:right+1]
        return s[left:right+1]

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is '':
            if p is '*' or '':
                return True
            else:
                return False
        if '.' and '*' not in p:
            if s == p:
                return True
            else:
                return False
        else:
            try:
                i = j = 0
                while i < len(p):
                    if i == len(p)-1 and p[i] == '*':
                        return True
                    if p[i] != '.' and p[i] != '*':
                        if p[i] != s[j]:
                            return False
                        else:
                            i += 1
                            j += 1
                            continue
                    if p[i] is '.':
                        i += 1
                        j += 1
                    elif p[i] is '*':
                        if p[i+1] is '*':
                            i += 1
                            continue
                        while True:
                            if s[j] == p[i+1]:
                                i += 2
                                break
                            else:
                                j += 1
            except IndexError:
                return False
            return True

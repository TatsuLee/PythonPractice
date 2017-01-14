#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                if (i == ')' and stack[-1] != '(') or \
                        (i == ']' and stack[-1] != '[') or \
                        (i == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return not stack 

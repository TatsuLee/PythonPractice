#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '' or num2 == '':
            return str(0)
        if num1 == '1' or num2 == '1':
            return max(num1,num2)
        product1,digit1 = 0,0
        for i in num1[::-1]:
            product2,digit2 = 0,0
            for j in num2[::-1]:
                product2 += int(i)*int(j)*(10**digit2)
                digit2 += 1
            product1 += product2*(10**digit1)
            digit1 +=1
        return str(product1)

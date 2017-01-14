class Solution(object):

    # cartian product of string a and string b
    def cartProd(self, a, b):
        return [i+j for i in a for j in b]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pDict = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        if digits:
            res = pDict[digits[0]]
        else:
            return []
        for i in digits[1:]:
            res = self.cartProd(res, pDict[i])
        return res

class Solution(object):

    def countAndSay(self, n):

        """
        :type n: int
        :rtype: str
        """
        res = ['', '1']
        if n < 2:
            return res[n]
        res, stack = '11', ''
        while n > 2:
            k = 1
            for i in range(1, len(res)):
                if res[i] == res[i-1]:
                    k += 1
                else:
                    stack += str(k)+res[i-1]
                    k = 1
                if i == len(res)-1:
                    stack += str(k)+res[i]
            res, stack = stack, ''
            n -= 1
        return res

class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, res[0], res[1] = [0 for i in range(n+1)], 1, 1
        if n < 2:
            return res[n]
        res[2] = 2
        for i in range(3, n+1):
            for j in range((i-1)/2):
                res[i] += 2*res[j]*res[i-j-1]  # avoid repeatition
            res[i] += (2-i % 2)*res[j+1]*res[i-j-2]  # odd/even fix
        return res[n]

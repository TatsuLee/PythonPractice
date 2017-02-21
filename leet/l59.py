class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = range(n*n, 0, -1)
        res, i, j = [[0 for k in range(n)] for k in range(n)], 0, n
        try:
            while nums != []:
                for k in range(j):
                    res[i][i+k] = nums.pop()
                for k in range(1, j):
                    res[i+k][n-1-i] = nums.pop()
                for k in range(1, j):
                    res[n-1-i][n-1-i-k] = nums.pop()
                for k in range(1, j-1):
                    res[n-1-i-k][i] = nums.pop()
                j -= 2
                i += 1
            return res
        except:
            return res

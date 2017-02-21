class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m*n == 0:
            return 0
        dp = [[0 for k in range(n)] for k in range(m)]
        # init boundary condition
        dp[0] = [1 for k in range(n)]
        for k in range(m):
            dp[k][0] = 1
        # forward calulating using difference equations
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

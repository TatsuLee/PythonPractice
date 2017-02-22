class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m*n == 0:
            return 0
        # dp_ij be num of paths to node ij
        dp = [[1 if i*j == 0 else 0 for j in range(n)] for i in range(m)]
        # forward calulating using difference equations
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

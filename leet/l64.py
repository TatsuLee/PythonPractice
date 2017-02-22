class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        # dp[i][j] be no. of paths to node i,j
        dp = grid
        # dp_ij be cumulative sum of nums of paths to node ij
        # forward calulating using difference equations
        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i][j-1], dp[i-1][j])
        return dp[m-1][n-1]

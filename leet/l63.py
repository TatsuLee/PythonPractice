class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):

        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if len(obstacleGrid) == 0:
            return 0
        else:
            m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp[i][j] be no. of paths to node i,j
        # forward calulating using difference equations
        dp = [[1 if i*j == 0 else 0 for j in range(n)] for i in range(m)]
        mflag, nflag = 0, 0
        for i in range(m):
            if mflag or obstacleGrid[i][0] == 1:
                dp[i][0], mflag = 0, 1
        for j in range(n):
            if nflag or obstacleGrid[0][j] == 1:
                dp[0][j], nflag = 0, 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

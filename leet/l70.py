class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        # let dp_i be # of ways to node i
        dp = [1 for i in range(n)]
        # set boundary conditions
        for i in range(2, n-1):
            dp[i] = dp[i-1] + dp[i-2]
        return 2*dp[i] + dp[i-1]

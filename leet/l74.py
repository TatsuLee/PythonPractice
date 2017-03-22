class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # method 1
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        l, r = 0, m-1
        while l-1 < r:
            mid = (l+r)/2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l += 1
            else:
                r -= 1
        if matrix[l-1][-1] < target:  # out of bin
            return False
        l1, r1 = 0, n-1
        while l1-1 < r1:
            mid = (l1+r1)/2
            if matrix[l-1][mid] == target:
                return True
            elif matrix[l-1][mid] < target:
                l1 += 1
            else:
                r1 -= 1
        return False
    # method 2: check l240

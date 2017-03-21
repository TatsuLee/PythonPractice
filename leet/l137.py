class Solution(object):

    # binary vector
    """
    def singleNumber(self, nums):
        n = 16
        bitVector, res = [0 for j in xrange(n)], 0
        # for each ith digit, check all nums
        for i in xrange(n):
            for j in nums:
                if (j >> i) & 1 == 1:
                    bitVector[i] = (bitVector[i]+1) % 3
            res |= bitVector[i] << i  # 0 or 1 << i
        # to deal with -, python only
        if bitVector[n-1] == 1:
            return res - 2**n
        return res
    """
    # hashtable
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitVector, res = [0 for j in xrange(n)], 0
        # for each ith digit, check all nums
        for i in xrange(n):
            for j in nums:
                if (j >> i) & 1 == 1:
                    bitVector[i] = (bitVector[i]+1) % 3
            res |= bitVector[i] << i  # 0 or 1 << i
        # to deal with -, python only
        if bitVector[n-1] == 1:
            return res - 2**n
        return res

class Solution(object):

    def canJump(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        i = len(nums)-2
        if i <= -1:
            return True
        if nums[0] == 0:
            return False
        while i > 0:
            if nums[i] == 0:
                j = i-1
                while j >= 0:
                    if nums[j] > i-j:
                        i = j
                        break
                    j -= 1
                if j < 0:
                    return False
            i -= 1
        return True

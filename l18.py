class Solution(object):

    def fourSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                # note that nums_i & j can be same value
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    tmpsum = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmpsum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif tmpsum < target:
                        l += 1
                    else:
                        r -= 1
        return res

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.subTrees(1, n)

    def subTrees(self, start, end):
        res = []
        if start > end:
            return [None]
        for rootval in range(start, end+1):
            leftSub = self.subTrees(start, rootval-1)
            rightSub = self.subTrees(rootval+1, end)
            for i in leftSub:
                for j in rightSub:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

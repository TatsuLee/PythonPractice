# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def dfs(self, root, d):
        if root is None:
            return d, True
        dl, flag = self.dfs(root.left, d+1)
        if not flag:
            return dl, False
        dr, flag = self.dfs(root.right, d+1)
        if not flag:
            return dr, False
        return max(dl, dr), abs(dl-dr) < 2

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.dfs(root, 0)[1]

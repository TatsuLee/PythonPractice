# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # recursive
    def dfs(self, root):
        if root is None:
            return [], True
        lval, flag = self.dfs(root.left)
        if not flag:
            return root.val, False
        rval, flag = self.dfs(root.right)
        if not flag:
            return root.val, False
        x = sorted(lval+rval+[root.val])
        if lval == rval == []:
            return [root.val], True
        if lval == [] and rval != []:
            return [x[0], x[-1]], (root.val < min(rval))
        if lval != [] and rval == []:
            return [x[0], x[-1]], (max(lval) < root.val)
        return [x[0], x[-1]], (max(lval) < root.val < min(rval))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.dfs(root)[1]

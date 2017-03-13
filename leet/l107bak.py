# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    res = []

    def depth(self, root):
        if root is None:
            return 0
        else:
            l = self.depth(root.left)
            r = self.depth(root.right)
            return max(l, r)+1

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = self.depth(root)
        for i in range(1, level+1):
            self.levelTraversal(root, i)
        return self.res

    def levelTraversal(self, root, level):
        if root is None:
            return
        if level == 1:
            self.res[level].append(root.val)
        else:
            self.levelTraversal(root.left, level-1)
            self.levelTraversal(root.right, level-1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res, clevel, nlevel = [[]], [root], []
        while True:
            for node in clevel:
                res[-1].append(node.val)
                if node.left:
                    nlevel.append(node.left)
                if node.right:
                    nlevel.append(node.right)
            # traversal on next level
            if nlevel == []:
                return res
            clevel = nlevel
            nlevel = []
            res.append([])

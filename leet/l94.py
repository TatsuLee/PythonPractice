# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # recursive
"""
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val]\
                + self.inorderTraversal(root.right)
"""

    # iterative, faster
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, current, res = [], root, []
        while True:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                    res.append(current.val)
                    current = current.right
                else:
                    return res

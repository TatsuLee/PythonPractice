# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # iterative
    """
    def preorderTraversal(self, root):

        stack, res = [root], []
        if root is None:
            return res
        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return res
    """
    # recursive
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)



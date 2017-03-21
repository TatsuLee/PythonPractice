# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # iterative
    """
    def maxDepth(self, root):
        if root is None:
            return 0
        stack, stack1, k = [root], [], 1
        while True:
            while stack:
                i = stack.pop()
                if i.left:
                    stack1.append(i.left)
                if i.right:
                    stack1.append(i.right)
            if stack1:
                k += 1
                stack, stack1 = stack1, []
            else:
                return k
    """

    # recursive
    def dfs(self, root, d):
        if root is None:
            return d
        return max(self.dfs(root.left, d+1),self.dfs(root.right, d+1))
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

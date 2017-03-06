# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # recursive
    """
    def postorderTraversal(self, root):
        if root is None:
            return []
        return self.postorderTraversal(root.left)\
                + self.postorderTraversal(root.right)+ [root.val]

    # iterative - 2 stacks
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack1, stack2 = [root], []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        return [i.val for i in stack2[::-1]]
    """
    # iterative - 1 stack
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack, current, res = [], root, []
        while True:
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            current = stack.pop()
            topStack = None if len(stack) < 1 else stack[-1]
            if current.right and current.right == topStack:
                stack.pop()
                stack.append(current)
                current = current.right
            else:
                res.append(current.val)
                current = None
            if len(stack) < 1:
                break
        return res

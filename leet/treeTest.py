import l98
# import l102  # level order traversal


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
#root.left.left.left = TreeNode(8)
test = l98.Solution()
out = test.isValidBST(root)
print out

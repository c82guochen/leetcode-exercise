class Solution(object):
    # using upper and lower bound is also an effectve way to pass values through the whole trees.
    def valid(self, node, left, right):
        if not node:
            return True
        if not ((node.val < right) and (node.val > left)):
            return False
        # Here you can see: for left subtrees, the node.val is the upper bound
        # For right subtrees, node.val is the lower bound.
        return (self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right))
    def isValidBST(self, root):
        return self.valid(root, float("-inf"), float("inf"))

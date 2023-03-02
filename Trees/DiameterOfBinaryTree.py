class Solution(object):
    def maxDeepth(self,root):
        if root == None:
            return 0
        return 1 + max(self.maxDeepth(root.left), self.maxDepth(root.right))
    def diameterOfBinaryTree(self, root):
        if root == None:
            return 0
        return self.maxDeepth(root.left) + self.maxDeepth(root.right) - 2
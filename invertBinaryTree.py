class Solution(object):
    #use DFS algorithm
    def invertTree(self, root):
        # firstly, should consider the edge case/base case
        if root == None:
            return 
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        # recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

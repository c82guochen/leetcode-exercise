class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        # Firstly, if preorder or inorder is empty, the tree doesn't have any nodes, so the algorithm returns None
        if not preorder or not inorder:
            return None 
        # The first node of preorder must be the root
        root = TreeNode(preorder[0])
        # The number of nodes in left subtree is mid (mid = mid-1+0+1), because mid is the position of root in preorder
        mid = inorder.index(preorder[0])
        # According to mid position, recursion can be conducted on left subtrees and right subtrees with subarray of preorder and inorder.
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

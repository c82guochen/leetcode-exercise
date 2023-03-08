# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # In this question, we should consider the features of binary tree
        cur = root
        while cur:
            # if all values are larger than cur, the lowest common ancestor must be in its right subtree
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            # if all values are smaller than cur, the lowest common ancestor must be in its left subtree
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            # Otherwise, one must be in cur's left subtree and another must be cur's right tree 
            # So their lowest common ancestor must be cur
            # including the edge case: one is cur, another is larger, so their LCA must be cur
            else:
                return cur
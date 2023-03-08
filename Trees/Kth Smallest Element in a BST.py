class Solution:
    def kthSmallest(self, root, k):
        n = 0
        stack = []
        cur = root
        # Here we use inorder transversal and stack
        while cur or stack:
            # if the current node has left child, then we iterate, because the left child must be the smallest
            while cur:
                stack.append(cur)
                cur = cur.left
            # Then we have a check that if the cur is the kth smallest node
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            # if not, we consider its right child before considering its parent
            # because in inorder traversal, left < node < right < node.parent
            cur = cur.right

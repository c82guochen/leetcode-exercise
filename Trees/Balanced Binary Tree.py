class Solution(object):
    # determine if it is balanced
    # means the  subtrees of "all nodes" are all balanced(difference less than 1)

    #PS: the reason we balance the binary tree is that balanced tree has much higher search efficiency
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def isBalanced1(self, root):
        if root == None:
            return True # If a node is None, 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return abs(left - right) <= 1 and self.isBalanced1(root.left) and self.isBalanced1(root.right)
        # not only this node but also its children, so remember and its children
        # Time complexity: O(n^2) because the algotithm does DFS for every subtree
                                        
    #Better solution: visit each node at most once
    def DFS(self, root):
        if root == None:
            return [True, 0]
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        balanced = (abs(left[1] - right[1]) <= 1) and left[0] and right[0]
        return [balanced, max(left[1], right[1]) + 1]

    def isBalanced(self,root):
        if root == None:
            return [True, 0]
        return (self.DFS(root))[0]
    # Sometimes bottom-up algorithm are more effective than top-down one.
    # Time complexity: O(n)  Space complexity: O(n)

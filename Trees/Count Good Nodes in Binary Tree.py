class Solution(object):
    def DFS(self, root, maxVal):
        if not root:
            return 0 
        # Fot this step, the same operation should be done for every root
        # if root.val >= maxVal:
        #     maxVal = root.val
        #     res = 1
        # else:
        #     res = 0
        # It's a more clear code
        res = 1 if root.val >= maxVal else 0
        maxVal = max(maxVal, root.val)
        # It means when code executes on this node, no larger node is found.So it's good.
        return res + self.DFS(root.left,maxVal) + self.DFS(root.right,maxVal)
        
    def goodNodes(self, root):
        maxVal = root.val
        return self.DFS(root, maxVal)

        
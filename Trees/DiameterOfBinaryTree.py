class Solution(object):
    def DFS1(self,root):
        if root == None:
            return -1   
            # Because the height of leaves is set to 0,
            # the height of none node is -1  
        left = self.DFS1(root.left)
        right = self.DFS1(root.right)
        self.ans = max(self.ans, left + right + 2)
        # So diameter is L+1+R+1 = L+R+2
        # (here 2 because we consider two children for all nodes) 
        return 1 + max(left,right)
    
    def DFS2(self,root):
        # Or we can consider this rule: 
        # the diameter of a root = the sum of depths of its left and right children
        # And the height/depth of a root is max(L, R) + 1
        if not root:
            return 0    # the exit of recursion
        left = self.DFS2(root.left) #do the same things to the left and right children
        right = self.DFS2(root.right)
        self.ans = max(self.ans, left + right) #update the max diameter we get
        return 1 + max(left, right)    #update the height    
        
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        if root == None:
            return 0
        # self.DFS1(root)
        self.DFS2(root)
        return self.ans
    # The mistake I made is just cosidering the root, but the longest diameter may not go through the root of the tree
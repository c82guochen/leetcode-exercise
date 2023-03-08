class Solution(object):
    
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
    # This algorithm is not correct for this problem for example ([1,1], [1])
    def isSubtree1(self, root, subRoot):
        if root == subRoot == None:
            return True
        elif root == None or subRoot == None:
            return False
        else:
            # Here is the error: 
            # if the root has the same value with its children,
            # the algoithm won't continue executing
            if root.val == subRoot.val:
                return self.isSameTree(root, subRoot)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSubtree2(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        # It should be like this:
        # only when isSameTree(root, subRoot) is true, return True(It considers all children)
        # 不会因为root和subroot值一样就停下来
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree2(root.left, subRoot) or self.isSubtree2(root.right, subRoot)


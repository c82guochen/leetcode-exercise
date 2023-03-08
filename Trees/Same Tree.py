class Solution(object):
    def isSameTree(self, p, q):
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSameTree2(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
        # (p is q) checks if p and q reference to the same object. 
        # In this case, if both p and q reference to None, then it is the same object so will return True, else False. 
        # It handles the part where p or q isn't exist so isn't handled by the first condition.
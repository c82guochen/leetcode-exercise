from collections import deque


class Solution(object):
    # DFS recursion
    def maxDepth1(self, root):
        # base case
        if not root :
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # Time complexity: O(n) Space complexity:O(height of tree)
        #606: Tree?

    # BFS iteration (with queue)
    def maxDepth2(self, root):
        if not root:
            return 0
        level = 0
        q = deque([root])
        # deque is a kind of queue that can be modified both sides
        while q:
            for i in range(len(q)):
                node = q.popleft() 
                #pop an item from the leftmost to variable node by popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                #Then add children to queue
            level += 1
        return level
    
    # DFS iteration(emulate the recursion stack)
    def maxDepth3(self, root):


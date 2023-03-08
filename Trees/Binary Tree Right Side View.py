import collections


class Solution(object):
    def rightSideView(self, root):
        ans = []
        q = collections.deque([root])
        while q:
            tmp = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    tmp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if tmp: #This step is very important, pay attention!!
                ans.append(tmp[-1])
        return ans
    
    # Here it's a more simple method
    def rightSideView1(self, root):
        ans = []
        q = collections.deque([root])
        while q:
            rightSide = None
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    rightSide = cur
                    q.append(cur.left)
                    q.append(cur.right)
            # You know, the rightSide is the last variable in all nodes with the same depth
            # It also means it's the rightmost one
            if rightSide: 
                ans.append(rightSide.val)
        return ans
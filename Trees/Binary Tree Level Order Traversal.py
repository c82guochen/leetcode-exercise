from collections import deque


class Solution(object):
    def levelOrder(self, root):
        q = deque([root])
        ans = []
        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    tmp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    # We don't judge if the children are None, so None will be put in q
                    # So we need consider extra [] because of None
            # This step is very important,remove the extra [] in ans.
            # [] can be brought by input [] or all items in q are None.
            if tmp: 
                ans.append(tmp)
        return ans

        
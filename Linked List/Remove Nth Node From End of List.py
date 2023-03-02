class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left, right = dummy, head
        # multiple pointers 
        # let the faster one initialized by head jump n times firstly
        while n > 0 and right:
            right = right.next
            n -= 1
        # Then jump togather until the faster one become the end(None)
        while right:
            left = left.next
            right = right.next
        # The left.next is the one we want to delete
        left.next = left.next.next
        # there are n+1 nodes between faster and slower
        # So when the faster one become None, 
        #the deleted one is the next node of slower. 

        return dummy.next
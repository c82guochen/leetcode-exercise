import math


class Solution(object):
    def kClosest(self, points, k):
        # I think the solution may use hashmap, but we can heapify a dict, so we can use list pairs
        minHeap = []
        # for point in points:
        for x, y in points:
            dist = x ** 2 + y ** 2
            minHeap.append([dist, x, y])
        # The heapify can heap one list according to its first item
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
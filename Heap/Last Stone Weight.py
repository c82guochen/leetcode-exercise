class Solution(object):
    def lastStoneWeight(self, stones):
        # python doesn't have MaxHeap, so we use MinHeap to simulate - use their opposite values
        minHeap = []
        # for e in stones:
        #     minHeap.append(-e)
        minHeap = [-e for e in stones]
        # It's a shorter and clearer experssion
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            l = heapq.heappop(minHeap)
            sl = heapq.heappop(minHeap)
            heapq.heappush(minHeap, l - sl)
        # Remember you should return absolute value
        return abs(minHeap[0])
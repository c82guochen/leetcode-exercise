class KthLargest(object):

    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k
        # heap: a more effective priority queue that can return/ delete the minimun value anytime
        heapq.heapify(self.minHeap)
        # we use heapq.heapify to initialize
        while len(self.minHeap) > k:
            # we use heapq.heappop to pop the minimum value
            heapq.heappop(self.minHeap)
        
    def add(self, val):
        # we use heapq.heappush to add values to heap
        heapq.heappush(self.minHeap, val)
        # If the length of our heap is larger than k, just remove the minimun value
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] 
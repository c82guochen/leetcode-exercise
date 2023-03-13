class Solution(object):
    # The first method is simple, because it uses heap
    def findKthLargest(self, nums, k):
        minHeap = nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return minHeap[0]

    # If we donot use heap, we need to use quicksort
    def findKthLargest2(self, nums, k):
        # If we need to get the Kth largest value by quicksort, we will put len(nums) - k in left smaller part
        k = len(nums) - k
        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l, r):
                # It means we put nums[i] into left part if nums[i] < pivot
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # After the for iteration, we put the pivot into its position(swap it and last item in nums)
            nums[p], nums[r] = pivot, nums[p]

            # Then we compare p and k
            # if p > k, we should continue finding in left part
            if p > k: return quickSelect(l,p-1)
            # if p < k, which means we haven't found the kth item yet, 
            # we should use recursion to continue finding in right part
            if p < k: return quickSelect(p+1,r)
            # Otherwise, we find the Kth largest value
            else:   return nums[p]

        return quickSelect(0, len(nums) - 1)
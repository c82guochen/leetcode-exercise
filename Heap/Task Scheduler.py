from collections import Counter, deque
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        # We use counter to count the number of different items in iterable object 
        # nums = [1, 1, 1, 6, 6, 6, 7, 8]
        # count = Counter(nums)  # 统计词频
        # count = Counter({1: 3, 6: 3, 7: 1, 8: 1})
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #pairs of [-cnt|idleTime]

        while maxHeap or q: 
            # It means we should detect if there is a task needed to be processed
            time += 1
            # use 1 time unit to process one task
            if maxHeap:
                # One task is processed, we remove that
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    # if cnt != 0, add it to queue(means the tasks will be processed later)
                    # if cnt == 0, jump this step(means all the same tasks are done) 
                    q.append([cnt, time + n])
            # if q[0][1] == time, it means the next time is for this task to be processed, so we put it into the maxHeap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
            
from collections import defaultdict
import heapq

    
class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetsMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweetsMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetsMap:
                minHeap.extend(self.tweetsMap[followeeId][-10:])
                
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            res.append(heapq.heappop(minHeap)[1])
        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
# twitter = Twitter()
# twitter.postTweet(1, 5)
# twitter.getNewsFeed(1)
# twitter.follow(1, 2)
# twitter.postTweet(2, 6)
# twitter.getNewsFeed(1)
# twitter.unfollow(1, 2)
# twitter.getNewsFeed(1)
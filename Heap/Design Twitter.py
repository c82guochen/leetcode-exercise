from collections import defaultdict
import heapq

# There is a situation that I don't consider: There exists users not be initiaized firstly
class User(object):
    def __init__(self, id = 0):
        self.userId = id
        self.tweets = [] # tweets posted by this user(tweetId list)
        self.follows = [] # userId list that the user is following
    
class Twitter(object):

    def __init__(self):
        self.time = 0
        self.users = defaultdict(list)

    def postTweet(self, userId, tweetId):
        if userId not in self.users:
            user = User(userId)
            self.users[userId] = user
        self.users[userId].tweets.append([self.time, tweetId])

        self.time -= 1

    def getNewsFeed(self, userId):
        tweets = []
        if userId not in self.users:
            user = User(userId)
            self.users[userId] = user
        for t in self.users[userId].tweets:
            tweets.append(t)
        for u in self.users[userId].follows:
            if u not in self.users:
                user = User(u)
                self.users[u] = user
            tweets += self.users[u].tweets
        heapq.heapify(tweets)
        realFeeds = []
        while len(realFeeds) < 10 and tweets:
            realFeeds.append(heapq.heappop(tweets)[1])
        return realFeeds

    def follow(self, followerId, followeeId):
        if followerId not in self.users:
            user = User(followerId)
            self.users[followerId] = user
        if followeeId not in self.users[followerId].follows:
            self.users[followerId].follows.append(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.users[followerId].follows:
            self.users[followerId].follows.remove(followeeId)

        
twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 3) 
twitter.postTweet(1, 101) 
twitter.postTweet(1, 12) 
twitter.postTweet(1, 10) 
twitter.postTweet(1, 2)
twitter.postTweet(1, 94)
twitter.postTweet(1, 505)
twitter.postTweet(1, 333)
twitter.postTweet(1, 22)
twitter.postTweet(1, 11)
twitter.getNewsFeed(1)

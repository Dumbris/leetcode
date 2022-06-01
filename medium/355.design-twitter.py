from collections import defaultdict 
import heapq

class Twitter:

    def __init__(self):
        self.followers = defaultdict(list)
        self.news = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.news[userId].append((-1*self.counter,tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        li = []
        heapq.heapify(li)
        for news in self.news[userId]:
                heapq.heappush(li,news)
                
        for followeeId in self.followers[userId]:
            for news in self.news[followeeId]:
                heapq.heappush(li,news)
        
        return [i[1] for i in heapq.nsmallest(10, li)]
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId) 


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
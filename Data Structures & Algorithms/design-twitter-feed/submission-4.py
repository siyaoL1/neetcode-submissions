import time
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((time.time(), tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId].copy()
        users.add(userId)
        
        heap = []
        for user in users:
            user_posts = self.posts[user]
            if user_posts:
                heapq.heappush_max(heap, (user_posts[-1], len(user_posts) - 1))
        
        res = []
        while heap and len(res) < 10:
            (_, tweetId, userId), post_index = heapq.heappop_max(heap)
            res.append(tweetId)
            next_post_index = post_index - 1
            if next_post_index >= 0:
                heapq.heappush_max(heap, (self.posts[userId][next_post_index], next_post_index))

        return res    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

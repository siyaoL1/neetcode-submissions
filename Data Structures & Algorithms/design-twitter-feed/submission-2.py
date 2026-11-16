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
        next_post_index = {}
        
        heap = []
        for user in users:
            user_posts = self.posts[user]
            if user_posts:
                heapq.heappush_max(heap, user_posts[-1])
                next_post_index[user] = len(user_posts) - 2
        
        res = []
        while heap and len(res) < 10:
            _, tweetId, userId = heapq.heappop_max(heap)
            res.append(tweetId)
            next_index = next_post_index[userId]
            if next_index >= 0:
                heapq.heappush_max(heap, self.posts[userId][next_index])
                next_post_index[userId] -= 1

        return res    

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

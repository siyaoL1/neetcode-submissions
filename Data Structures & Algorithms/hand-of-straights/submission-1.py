class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)
        while heap:
            curr = heap[0]
            for num in range(curr, curr + groupSize):
                if num in count:
                    count[num] -= 1
                    if count[num] == 0:
                        if heap[0] != num:
                            return False
                        heapq.heappop(heap)
                        count.pop(num)
                else:
                    return False

        return True

        